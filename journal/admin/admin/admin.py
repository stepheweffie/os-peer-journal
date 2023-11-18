from wtforms import TextAreaField
from flask_admin.actions import action
from forms import UploadForm, CKTextAreaWidget, ReviewForm, SettingsForm
from flask.views import MethodView
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, request, jsonify, flash
from flask_login import current_user
from flask_admin import AdminIndexView, expose_plugview, expose
import os
import datetime
from models import db, Paper, User
from submissions.app import Review
from flask_admin.form import rules
from jinja2 import Environment
import json
from flask_wtf.csrf import generate_csrf

# Might not need this extra env stuff now
def extract_filename(path):
    return path.split('/')[-1]  # Split by '/' and get the last part


# Create a Jinja2 environment and add the custom filter
jinja_env = Environment()
jinja_env.filters['extract_filename'] = extract_filename


directory_path = 'submissions/papers/uploads'  # Replace with your actual directory path
submitted_files = []
try:
    for root, _, filenames in os.walk(directory_path):
        for filename in filenames:
            submitted_files.append(os.path.join(root, filename))
except OSError as e:
    jsonify(error=str(e))


class AdminIndex(AdminIndexView):
    @expose('/', methods=['GET', 'POST'])
    def index(self):
        # Handles a BaseForm instance (differently than a FlaskForm instance)
        form = UploadForm()

        papers = Paper.query.filter(Paper.user_id != current_user.id).all()

        papers_data = [
            {"id": paper.id, "title": paper.title, "authors": paper.authors}
            for paper in papers
        ]

        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        if not current_user.is_admin and request.method == 'GET':
            return self.render('admin/index.html', form=form, data=papers_data)
        if current_user.is_admin and request.method == 'GET':
            return self.render('admin/admin_index.html', form=form, data=papers_data)

        if request.method == 'POST':
            form.process(request.form)
            csrf_token = request.form.get('csrf_token')

            if form.validate():
                if 'review' in request.form:
                    title = request.form.get('title')
                    return redirect('/admin/write_review', csrf_token=csrf_token, title=title)

                upload = request.files['file']
                if upload is None or upload.filename == '':
                    flash('No selected file', 'danger')
                    return redirect('/admin')
                paper = Paper(
                              title=form.title.data,
                              authors=form.authors.data,
                              abstract=form.abstract.data,
                              timestamp=form.timestamp,
                              file=upload.filename,
                              under_review=False,
                              user_id=current_user.id)

                db.session.add(paper)
                db.session.commit()
                upload.save(os.path.join(directory_path, upload.filename))
                flash('Your paper has been submitted successfully!', 'success')
                return redirect('/admin/submitted_papers')
            flash('Invalid form submission', 'danger')


    @expose_plugview('/submitted_papers')
    class SubmittedPapers(MethodView):
        def __init__(self, files=None):
            # Check if current_user is not None and has the papers attribute
            if current_user and hasattr(current_user, 'papers'):
                self.files = current_user.papers
            else:
                self.files = []

        def get(self, cls):
            return cls.render('submitted_papers.html', request=request, name="GET Your Papers", files=self.files)

        def post(self, cls):
            return cls.render('submitted_papers.html', request=request, name="POST Your Papers", files=self.files)

    @expose_plugview('/reviews')
    class Reviews(MethodView):
        def __init__(self, files=None):
            self.files = Paper.query.filter_by(reviewer=current_user.email).all()

        def get(self, cls):
            return cls.render('reviewed_papers.html', request=request, name="GET Review", files=self.files)

        def post(self, cls):
            return cls.render('reviewed_papers.html', request=request, name="POST Review", files=self.files)

    @expose_plugview('/published_papers')
    class Published(MethodView):
        def __init__(self, files=None):
            # Check if current_user is not None and has the papers attribute
            if current_user and hasattr(current_user, 'papers'):
                papers = current_user.papers
                self.files = [p for p in papers if p.published]
            else:
                self.files = []

        def get(self, cls):
            return cls.render('published_papers.html', request=request, name="GET Published", files=self.files)

    @expose("/user_password", methods=["GET", "POST"])
    def user_password(self):
        form = request.form.to_dict()
        if request.method == 'POST':
            if len(form['newpassword']) < 6:
                flash('Password must be at least 8 characters long!', 'danger')
                return redirect('/login')
            user = User.get_one(email=current_user.email)
            user.change_password(user.email, form['newpassword'])
            user.save()
            flash('Your password has been updated!', 'success')
        return redirect('/admin')

    @expose('/settings', methods=['GET', 'POST'])
    def settings(self):
        form = SettingsForm()
        if request.method == 'POST':
            if form.first_name.data:
                current_user.first_name = form.first_name.data
            if form.last_name.data:
                current_user.last_name = form.last_name.data
            if form.email.data:
                current_user.email = form.email.data
            if form.website.data:
                current_user.website = form.website.data
            db.session.commit()
            flash('Your settings have been updated!', 'success')
            return redirect('/admin')
        return self.render('settings.html', request=request, name="Settings", form=form)

    @expose('/write_review', methods=['GET', 'POST'])
    def write_review(self):
        # handle the form here and save the review
        csrf_token = request.form.get('csrf_token')
        title = request.form.get('title')
        try:
            paper_id = request.form.get('paper_id')
            paper = Paper.query.get(paper_id)
            paper = paper.title
        except AttributeError:
            paper = None

        form = ReviewForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                flash('Your review has been submitted successfully!', 'success')
                return redirect(Review.post)
        return self.render('user_write_review.html', form=form, paper=paper, title=title, csrf_token=csrf_token)

    @expose('/review_submissions')
    def get_review_submissions(self):
        # Return the list of current submissions for review as JSON data
        files = Paper.query.filter(Paper.user_id != current_user.id).all()
        data = {
            "total": len(files),  # Total number of records
            "totalNotFiltered": len(files),  # Total number of records without filtering
            "rows": [
                {
                    "id": file.id,
                    "title": file.title,
                    "authors": file.authors
                }
                for file in files
            ]
        }
        json_data = json.dumps(data)
        return json_data

    @expose('/logout')
    def logout_user(self):
        return redirect(url_for('auth.logout'))


class UserModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        super().on_model_change(form, model, is_created)
        model.email = form.email.data
        model.first_name = form.first_name.data
        model.last_name = form.last_name.data
        model.is_admin = form.is_admin.data
        model.date_created = datetime.datetime.now()
        if is_created:
            model.set_password(form.password.data)
            model.save()
        if form.password.data:
            model.change_password(model.email, form.password.data)
        model.save()

    column_list = ('first_name', 'last_name', 'email', 'date_created')
    column_searchable_list = ('first_name', 'last_name', 'email', 'date_created')
    column_filters = ('first_name', 'last_name', 'is_admin', 'email', 'verified')
    form_excluded_columns = ('fs_uniquifier', 'password_hash', 'website', 'papers', 'date_created')
    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    page_size = 10
    column_editable_list = ('is_admin', 'first_name', 'last_name', 'email')


class PublishedPapersModelView(ModelView):
    column_list = ('title', 'authors', 'reviewed_by', 'review_date', 'filename', 'published', 'pub_date')
    column_searchable_list = ('title', 'authors', 'reviewed_by', 'review_date', 'filename')
    column_filters = ('title', 'authors', 'reviewed_by', 'review_date',  'filename', 'published', 'pub_date')
    form_excluded_columns = ('file', 'filepath', 'published_by')
    can_create = False
    can_edit = True
    can_delete = False
    can_export = True
    page_size = 10
    column_default_sort = ('pub_date', True)


class ReviewModelView(ModelView):
    @action('toggle_activation', 'Fail',
            'Sure you want to grade the paper?')
    def toggle_activation(self, titles):
        for t in titles:
            r = Review.query.get(t)
            if r:
                r.fail = not r.fail
                db.session.commit()

    def on_model_change(self, form, model, is_created):
        super().on_model_change(form, model, is_created)
        file_name = form.filename.data
        edit = model.query.filter_by(filename=file_name).first()
        edit.review = form.review.data
        edit.review_date = datetime.datetime.now()
        edit.reviewed_by = current_user.email
        edit.reviewed = True

        if is_created:
            db.session.add(model)
        db.session.commit()

    can_create = True
    can_edit = True
    can_delete = True
    can_export = True
    column_list = ('title', 'authors', 'reviewed_by', 'review_date', 'fail')
    column_searchable_list = ('title', 'authors', 'reviewed_by', 'review_date')
    column_filters = ('title', 'authors', 'reviewed_by', 'review_date', 'fail')
    form_excluded_columns = ('review_date', 'authors', 'title', 'reviewed_by', 'fail')
    create_template = 'write_review.html'
    form_extra_fields = {
        'review': TextAreaField('Review', widget=CKTextAreaWidget())}
    form_create_rules = [
        rules.HTML('<h2>Write A Review</h2>'),
        rules.HTML('<label for"filename"><h4>Review For: </h4></label>'
                   '<select name="filename" id="filename" '
                   'style="background:#edf2ff; width: 50%; margin: 5px; height: 40px; '
                   'padding: 5px; appearance: menulist-button; border: 6px solid transparent;">'),
        rules.HTML('<div id="editor">'
                   '<form class ="form-group" method="post" id="wysiwyg" action="/admin/reviewed_papers">'
                   '<textarea class ="form-control" id="editor" name="review" >'
                   '</textarea></form>'
                   '</div>'),
    ]


class SubmissionsModelView(ModelView):
    can_create = False
    can_edit = True
    can_delete = False
    can_export = True
    page_size = 10
    column_list = ('title', 'authors', 'timestamp', 'file', 'under_review', 'reviewer', 'user_id', 'published')
    column_default_sort = ('timestamp', True)
    column_searchable_list = ('title', 'authors', 'timestamp', 'file', 'reviewer', 'user_id')
    column_filters = ('title', 'authors', 'timestamp', 'file', 'under_review', 'reviewer', 'user_id', 'published')
    form_excluded_columns = ('file', 'filepath', 'published_by')
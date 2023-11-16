from wtforms import TextAreaField
from flask_admin.actions import action
from forms import UploadForm, CKTextAreaWidget
from flask.views import MethodView
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, request, jsonify, flash
from flask_login import current_user
from flask_admin import AdminIndexView, expose_plugview, expose
import os
import datetime
from models import db, Paper
from submissions.app import Review
from flask_admin.form import rules
from jinja2 import Environment
from file_utils import copy_papers

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
        if request.method == 'POST':
            form.process(request.form)
            if form.validate():
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
                              under_review=False)

                paper.user_id = current_user.id
                db.session.add(paper)
                db.session.commit()
                upload.save(os.path.join(directory_path, upload.filename))
                flash('Your paper has been submitted successfully!', 'success')
                return redirect('/admin/submitted_papers')
            flash('Invalid form submission', 'danger')
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        if not current_user.is_admin:
            return self.render('admin/index.html', form=form)
        return self.render('admin/admin_index.html', form=form)

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

    @expose_plugview('/reviewed_papers')
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

    @expose('/review_submissions')
    def get_review_submissions(self):
        # Return the list of current submissions for review as JSON data
        files = Paper.query.filter(Paper.user_id != current_user.id).all()
        return jsonify(files=files)

    @expose('/all_papers_ever')
    def get_all_papers_ever(self):
        # Return the list of all papers as JSON data
        files = Paper.query.all()
        return jsonify(files=files)

    @expose('/logout')
    def logout_user(self):
        return redirect(url_for('auth.logout'))


class UserModelView(ModelView):
    column_list = ('first_name', 'last_name', 'email', 'date_created')
    column_searchable_list = ('first_name', 'last_name', 'email', 'date_created')
    column_filters = ('first_name', 'last_name', 'is_admin', 'email', 'verified')
    form_excluded_columns = ('fs_uniquifier', 'password_hash')
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
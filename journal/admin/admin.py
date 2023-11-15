from wtforms import TextAreaField
from flask_admin.actions import action
from forms import UploadForm, CKTextAreaWidget
from flask.views import MethodView
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, request, jsonify
from flask_login import current_user
from flask_admin import AdminIndexView, expose_plugview, expose
import os
import datetime
from models import db
from submissions.app import Review
from flask_admin.form import rules
from jinja2 import Environment


def extract_filename(path):
    return path.split('/')[-1]  # Split by '/' and get the last part


# Create a Jinja2 environment and add the custom filter
jinja_env = Environment()
jinja_env.filters['extract_filename'] = extract_filename


directory_path = 'submissions/papers/uploads'  # Replace with your actual directory path
uploaded_files = []
try:
    for root, _, filenames in os.walk(directory_path):
        for filename in filenames:
            uploaded_files.append(os.path.join(root, filename))
except OSError as e:
    jsonify(error=str(e))


class AdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        form = UploadForm()
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        if not current_user.is_admin:
            return self.render('admin/index.html', form=form)
        return self.render('admin/index.html', form=form)

    @expose_plugview('/submitted_papers')
    class SubmittedPapers(MethodView):
        def __init__(self, files=uploaded_files):
            self.files = files  # Store the list of files as an instance variable

        def get(self, cls):
            return cls.render('submitted_papers.html', request=request, name="GET Paper", files=self.files)

        def post(self, cls):
            return cls.render('submitted_papers.html', request=request, name="POST Paper", files=self.files)

    @expose_plugview('/reviewed_papers')
    class Reviews(MethodView):
        def get(self, cls):
            return cls.render('reviewed_papers.html', request=request, name="GET Reviews")

        def post(self, cls):
            return cls.render('reviewed_papers.html', request=request, name="POST Review")

    @expose_plugview('/published_papers')
    class Reviews(MethodView):
        def get(self, cls):
            return cls.render('published_papers.html', request=request, name="GET Reviews")

        def post(self, cls):
            return cls.render('published_papers.html', request=request, name="POST Review")

    @expose('/submissions')
    def get_submissions(self):
        # Return the list of files as JSON data
        return jsonify(files=uploaded_files)

    @expose('/logout')
    def logout_view(self):
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


class PaperModelView(ModelView):
    column_list = ('title', 'authors', 'reviewed', 'reviewed_by', 'review_date', 'filename', 'published', 'pub_date')
    column_searchable_list = ('title', 'authors', 'reviewed_by', 'review_date', 'filename')
    column_filters = ('title', 'authors', 'reviewed', 'reviewed_by', 'review_date',  'filename', 'published', 'pub_date')
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
    column_filters = ('title', 'authors', 'reviewed_by', 'review_date')
    form_excluded_columns = ('review_date', 'authors', 'title', 'reviewed_by')
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

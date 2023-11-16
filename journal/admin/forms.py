from flask_admin.form import BaseForm
from flask_admin.form.upload import FileUploadField
from wtforms import TextAreaField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Length, Email
from flask_login import current_user
import datetime


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=80)])
    submit = SubmitField('Login')


class UploadForm(BaseForm):
    title = StringField('Paper Title', validators=[InputRequired(), Length(min=4, max=50)])
    abstract = TextAreaField('Abstract', validators=[InputRequired(), Length(min=4, max=500)])
    authors = StringField('Authors', validators=[InputRequired(), Length(min=4, max=50)])
    file = FileUploadField('Paper Submission Upload', namegen='', allowed_extensions=['pdf', 'ipynb'],
                           base_path='submissions/papers/uploads', allow_overwrite=True)
    timestamp = datetime.datetime.now()
    submit = SubmitField('Submit')


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        # add WYSIWYG class to existing classes
        existing_classes = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = '{} {}'.format(existing_classes, "ckeditor")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

from flask_admin.form import BaseForm
from flask_admin.form.upload import FileUploadField
from wtforms import TextAreaField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=80)])
    submit = SubmitField('Login')


class UploadForm(BaseForm):
    upload = FileUploadField('Paper Submission Upload', namegen='', allowed_extensions=['pdf', 'ipynb'],
                             base_path='submissions/papers', allow_overwrite=True)
    submit = SubmitField('Submit')


class PaperSelectForm(FlaskForm):
    filename = SelectField('Choose Paper', choices=[('option1', 'Option 1'), ('option2', 'Option 2')])


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        # add WYSIWYG class to existing classes
        existing_classes = kwargs.pop('class', '') or kwargs.pop('class_', '')
        kwargs['class'] = '{} {}'.format(existing_classes, "ckeditor")
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

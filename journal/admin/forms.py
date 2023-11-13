from flask_admin.form import BaseForm
from flask_admin.form.upload import FileUploadField
from wtforms import TextAreaField, SelectField, SubmitField
import os
import os.path as op


class UploadForm(BaseForm):
    upload = FileUploadField('Paper Submission Upload', namegen='', allowed_extensions=['pdf', 'ipynb'],
                             base_path='submissions/papers', allow_overwrite=False)


class ReviewForm(BaseForm):
    data = TextAreaField('Data')
    decision = SelectField('Decision', choices=[('accept', 'Accept'), ('reject', 'Reject')])
    submit = SubmitField('Submit Review')


# Create directory for file fields to use
file_path = op.join(op.dirname(__file__), 'files')
try:
    os.mkdir(file_path)
except OSError:
    pass




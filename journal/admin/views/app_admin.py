from flask_security import current_user
from flask import current_app as app # This is to access the app context
from flask import Blueprint
from flask_admin import AdminIndexView, expose
from flask import redirect, url_for
from models import User, db
import os
from functools import wraps
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import sys
from config import UPLOAD_FOLDER
sys.path.append('/')

from api import PublishedPapers

admin_blueprint = Blueprint('admin', __name__)


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        admin_email = app.config.get('ADMIN_EMAIL')
        if not current_user.is_authenticated or current_user.email != admin_email:
            return redirect(url_for('/'))
        return func(*args, **kwargs)
    return decorated_view


@admin_required
def logout():
    return redirect(url_for('security.logout'))


class SecureAdminView(AdminIndexView):
    @expose('/')
    @admin_required  # This is a Flask-Security decorator.
    def index(self):
        return super(SecureAdminView, self).index()


class UserModelView(ModelView):
    column_list = ('username', 'email')
    column_searchable_list = ('username', 'email')
    column_filters = ('username', 'email', 'active', 'authenticated')
    form_excluded_columns = ('fs_uniquifier', 'password_hash')

# Initialize Flask-Admin with the blueprint


admin = Admin(admin_blueprint, index_view=SecureAdminView(), template_mode='bootstrap3')
admin.add_view(FileAdmin(os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER), name='Uploaded Papers'))
admin.add_view(UserModelView(User, db.session))
admin.add_view(ModelView(PublishedPapers, db.session))











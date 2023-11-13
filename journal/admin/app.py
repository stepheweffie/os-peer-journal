from flask import Flask, redirect, url_for
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_migrate import Migrate
from models import db, User, bcrypt, ma
from config import UPLOAD_FOLDER
import os
from submissions.app import PublishedPapers
import datetime
from flask_bootstrap import Bootstrap5
from forms import UploadForm
from flask_wtf.csrf import CSRFProtect

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class AdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        form = UploadForm()
        papers = ['paper1', 'paper2', 'paper3']
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        if not current_user.is_admin:
            return self.render('admin/index.html', form=form, papers=papers)
        return self.render('admin/admin_index.html', form=form, papers=papers)


class UserModelView(ModelView):
    column_list = ('first_name', 'last_name', 'email', 'date_created')
    column_searchable_list = ('first_name', 'last_name', 'email', 'date_created')
    column_filters = ('first_name', 'last_name', 'is_admin', 'email', 'verified')
    form_excluded_columns = ('fs_uniquifier', 'password_hash')


def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    # Absolute path to config.py
    Bootstrap5(app)
    CSRFProtect(app)
    app.config.from_pyfile(config_filename)
    salt = os.urandom(16).hex()
    app.config['SECURITY_PASSWORD_SALT'] = salt
    app.config['FLASK_ADMIN_SWATCH'] = 'paper'
    db.init_app(app)
    login_manager.init_app(app)
    app.config['SESSION_TYPE'] = 'filesystem'
    bcrypt.init_app(app)
    admin = Admin(app, name='Admin', template_mode='bootstrap3', index_view=AdminIndex())
    admin.add_view(UserModelView(User, db.session))
    admin.add_view(FileAdmin(os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER), name='Uploaded Papers'))
    admin.add_view(ModelView(PublishedPapers, db.session))
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))
    return app


def create_database(app):
    with app.app_context():
        Migrate(app, db)
        db.create_all()
        # Marshmallow must come after db.create_all()
        ma.init_app(app)
        # Check if the admin user already exists
        admin_email = os.getenv('ADMIN_EMAIL')
        admin_pass = os.getenv('ADMIN_PASSWORD')
        admin = User.query.filter_by(email=f'{admin_email}').first()
        if not admin:
            admin = User(id='1', email=f'{admin_email}')
            admin.set_password(f'{admin_pass}')  # Set the password using your set_password method
            admin.is_admin = True  # Set the admin flag to True
            admin.date_created = datetime.datetime.now()
            # Create the admin user
            db.session.add(admin)
            db.session.commit()
            print('Admin user created successfully.')
        else:
            print('Admin user already exists.')


def init_app():
    config_path = os.getenv('FLASK_CONFIG_PATH')
    app = create_app(f'{config_path}')
    create_database(app)
    return app


if __name__ == '__main__':
    app = init_app()
    with app.app_context():
        app.run(port=5050, debug=True)
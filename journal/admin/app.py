from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_migrate import Migrate
from models import db, User, bcrypt
from config import UPLOAD_FOLDER
import os
from flask_bootstrap import Bootstrap5
from submissions.app import PublishedPapers

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class AdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


class UserModelView(ModelView):
    column_list = ('username', 'email')
    column_searchable_list = ('username', 'email')
    column_filters = ('username', 'email', 'active', 'authenticated')
    form_excluded_columns = ('fs_uniquifier', 'password_hash')


def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    salt = os.urandom(16).hex()
    app.config['SECURITY_PASSWORD_SALT'] = salt
    db.init_app(app)
    Bootstrap5(app)
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
        # Check if the admin user already exists
        admin = User.query.filter_by(email='admin@admin.com').first()
        if not admin:
            admin = User(id='1', username='admin', email='admin@admin.com')
            admin.set_password('secret')  # Set the password using your set_password method
            admin.is_admin = True  # Set the admin flag to True
            # Create the admin user
            db.session.add(admin)
            db.session.commit()
            print('Admin user created successfully.')
        else:
            print('Admin user already exists.')


def init_app():
    app = create_app('/Users/savantlab/PycharmProjects/savantlab_journal/journal/admin/config.py')
    create_database(app)
    return app


if __name__ == '__main__':
    app = init_app()
    with app.app_context():
        app.run(port=5050, debug=True)
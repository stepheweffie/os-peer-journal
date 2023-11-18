from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin
from flask_migrate import Migrate
from models import db, User, bcrypt, ma, Paper
from config import UPLOAD_FOLDER
import os
import datetime
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from admin import AdminIndex, UserModelView, PublishedPapersModelView, ReviewModelView, extract_filename, \
    SubmissionsModelView
from submissions.app import PublishedPapers, Review
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
    # Initialize flask-login
    app.config['SESSION_TYPE'] = 'filesystem'
    app.jinja_env.filters['extract_filename'] = extract_filename
    bcrypt.init_app(app)
    admin = Admin(app, name='Contribute', template_mode='bootstrap3', index_view=AdminIndex())
    admin.add_view(UserModelView(User, db.session))
    admin.add_view(FileAdmin(os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER), name='Uploaded Papers',
                             endpoint='uploaded'))
    admin.add_view(PublishedPapersModelView(PublishedPapers, db.session, endpoint='published_papers'))
    admin.add_view(ReviewModelView(Review, db.session, endpoint='paper_reviews'))
    admin.add_view(SubmissionsModelView(Paper, db.session, name='Submissions', endpoint='submissions'))
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))

    return app


def create_database(app):
    with app.app_context():
        Migrate(app, db)
        # db.drop_all()
        db.create_all()
        # Marshmallow must come after db.create_all()
        ma.init_app(app)
        # Check if the admin user already exists
        admin_email = os.getenv('ADMIN_EMAIL')
        admin_pass = os.getenv('ADMIN_PASSWORD')
        admin = User.query.filter_by(email=f'{admin_email}').first()
        if not admin:
            admin = User()
            admin.email = f'{admin_email}'
            admin.set_password(f'{admin_pass}')  # Set the password using your set_password method
            admin.is_admin = True  # Set the admin flag to True
            admin.date_created = datetime.datetime.now()
            # Create the admin user
            admin.save()
            print('Admin user created successfully.')
        if admin.is_admin is False:
            admin.is_admin = True
            admin.save()


def init_app():
    config_path = os.getenv('FLASK_CONFIG_PATH')
    admin_app = create_app(f'{config_path}')
    create_database(admin_app)
    return admin_app


if __name__ == '__main__':
    app = init_app()
    with app.app_context():
        app.run(port=5050, debug=True)
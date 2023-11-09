import os
from flask import request, Blueprint
from flask import current_app as app
from pywebio import session
from models import db, User, user_datastore
from flask_security import login_user, current_user
from pywebio.input import textarea, input, file_upload, input_group, radio
from pywebio.output import put_text
from pywebio.session import go_app
from .decorators import login_required_webio_view, user_required
from pywebio_battery import basic_auth
from pywebio.session import register_thread
import threading
from config import TARGET_DIR
from pywebio.platform.flask import webio_view


pywebio_logic_blueprint = Blueprint('pywebio_logic', __name__)


@pywebio_logic_blueprint.route("/logicio", methods=['GET', 'POST'])
# @app.route('/', methods=['GET', 'POST'])
def root():
    register_thread(thread=threading.current_thread())
    try:
        if not current_user.is_authenticated:
            go_app('register')
        elif current_user.is_authenticated:
            go_app('exchange')
    except AttributeError:
        # Handle the case where current_user or is_authenticated isn't available
        go_app('register')


@pywebio_logic_blueprint.route("/set_password", methods=['GET', 'POST'])
@user_required
def password_set():
    if request.method == 'GET':
        new_user = User.query.filter_by(email=session['email'], username=session['username']).first()
        if new_user:
            def check_password_creation(p, confirm_p):
                if p == confirm_p:
                    create_new_user = User.query.filter_by(email=session['email']).first()
                    create_new_user.set_password(confirm_p)
                    db.session.commit()
                    put_text('Password set successfully.')
                else:
                    put_text('Passwords do not match. Please try again.')

            password_creation = input_group("Create a password", [
                input("Password", name='password', type='password'),
                input("Confirm Password", name='confirm_password',
                      type='password', validate=check_password_creation)])

            if new_user.check_password(password_creation['password']):
                login_user(new_user)
                new_user.authenticated = True
                db.session.commit()
                go_app('/')
            else:
                put_text('Password creation failed. Please refresh and try again.')
                go_app('/')


@pywebio_logic_blueprint.route("/register", methods=['GET', 'POST'])
# @app.route('/register', methods=['GET', 'POST'])
def register():
    # register_thread(thread=threading.current_thread())
    try:
        try:
            with app.app_context():
                def check_form(data):
                    old_user = User.query.filter_by(username=data).first()
                    if old_user:
                        put_text('Username already exists. Please try again.')
                    old_user = User.query.filter_by(email=data).first()
                    if old_user:
                        put_text(f"User with email {data} already exists. Please try again.")

                def verify_login(login_email, login_password):
                    logging_in_user = User.query.filter_by(email=login_email).first()
                    if logging_in_user and logging_in_user.check_password(login_password):
                        return True
                    return False

                action = radio("What would you like to do?", options=['Login', 'Register'])

                if action == 'Register':
                    try:
                        if not current_user.is_authenticated:
                            registration = input_group("Register", [
                                input("Username", name='username', type='text', validate=check_form),
                                input("Email", name='email', type='text', validate=check_form)]
                                                       )
                            username = registration['username']
                            email = registration['email']
                            user_datastore.create_user(username=username, email=email, password=None)
                            session['email'] = email
                            session['username'] = username
                            db.session.commit()
                            # time to send an email with a link to set password and confirm email
                            put_text(
                                'Registration successful. Please check your email for a link to set your password.')
                            go_app('/verify_email')

                    except AttributeError:
                        go_app('/')

                elif action == 'Login':
                    try:
                        try:
                            if not current_user.is_authenticated:
                                pywebio_secret_key = os.urandom(32).hex()
                                # Returns the first parameter in lambda assumes is username
                                user_login = basic_auth(verify_login,
                                                        secret=pywebio_secret_key,
                                                        expire_days=10,
                                                        token_name='pywebio_token')

                                if user_login:
                                    logging_in = User.query.filter_by(email=user_login).first()
                                    if logging_in:
                                        login_user(logging_in)
                                        put_text(
                                            f"Hello, {logging_in.username}. You can refresh this page and see what happens.")
                                        go_app('exchange')
                        except RuntimeError:
                            go_app('/')
                    except AttributeError:
                        go_app('/')

        except RuntimeError:
            go_app('/register')
    except RuntimeError:
        go_app('/register')


@pywebio_logic_blueprint.route("/exchange", methods=['GET', 'POST'])
# @app.route('/exchange', methods=['GET', 'POST'])
@login_required_webio_view
def journal_app():
    # register_thread(thread=threading.current_thread())
    try:
        if current_user.is_authenticated:
            with app.app_context():
                action = radio("What would you like to do?", ["Submit a new article", "Review a new article", "Exit"])
                if action == "Submit a new article":
                    paper_data = input_group("Submit your paper", [
                        input('Title of the paper', placeholder="Paper Title", name="title"),
                        textarea('Abstract', placeholder="Abstract of the paper", name="abstract"),
                        input('Author(s)', placeholder="Author names separated by comma", name="authors"),
                        file_upload("Upload paper", name="file", accept=[".pdf", ".ipynb"]),
                    ])

                    file_info = paper_data.pop('file')
                    filename = file_info['filename']
                    content = file_info['content']
                    file_path = os.path.join(TARGET_DIR, filename)
                    with open(file_path, 'wb') as f:
                        f.write(content)
                        f.close()
                    put_text("Your paper has been submitted successfully")
                    go_app('/')
                elif action == "Review a new article":
                    put_text("Review a new article")
                    go_app('/')

    except AttributeError:
        # put_text("You are not logged in. Please refresh the page.")
        go_app('/register')


@pywebio_logic_blueprint.route("/verify_email", methods=['GET', 'POST'])
def verify_email():
    put_text('verify your email')



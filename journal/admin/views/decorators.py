from flask import url_for, session
from flask_security import current_user
from models import User
from functools import wraps
from pywebio.session import go_app


def login_required_webio_view(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated:  # Assuming you are using Flask-Login's current_user
            go_app('register')
        return func(*args, **kwargs)
    return decorated_view


def user_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if 'email' in session and 'username' in session:
            can_set = User.query.filter_by(email=session['email'], username=session['username']).first()
            if can_set and can_set.password is None:
                return func(*args, **kwargs)  # Return the result of the actual view function
            else:
                # If you want to redirect if the password is set or some other condition, do it here
                go_app(url_for('root'))  # Assuming the function for the '/' route is named `root`
                return
        else:
            go_app(url_for('root'))
            return

    return decorated_view

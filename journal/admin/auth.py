from flask import render_template, redirect, url_for, flash, Blueprint, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email
from flask_login import login_user, login_required, logout_user, current_user
from models import User, users_schema


auth = Blueprint('auth', __name__)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=80)])
    submit = SubmitField('Login')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if not current_user.is_authenticated:
        if request.method == 'POST':
            if form.validate_on_submit():
                email = request.form.get('email')
                password = request.form.get('password')
                user = User.query.filter_by(email=email).first()
                if user and user.check_password(password):
                    login_user(user)
                    # Redirect to the admin index route after successful login
                    return redirect(url_for('admin.index'))
        return render_template('login.html', form=form)
    # User is already authenticated, redirect them to the admin index
    return redirect(url_for('admin.index'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('auth.login'))


@auth.route("/api/users")
@login_required
def users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return {'users': result}


@auth.route("/api/papers")
@login_required
def papers():
    all_papers = User.query.all().papers
    result = users_schema.dump(all_papers)
    return {'papers': result}
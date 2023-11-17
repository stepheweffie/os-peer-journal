from flask import render_template, redirect, url_for, Blueprint, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from models import User, users_schema
from forms import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                login_user(user, remember=True, force=False, fresh=True)
                return redirect(url_for('admin.index'))
            return redirect(url_for('auth.login'))
    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))
    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/users")
@login_required
def users():
    if current_user.is_admin:
        all_users = User.get_all()
        result = users_schema.dump(all_users)
        return {'users': result}
    return redirect(url_for('auth.login'))


@auth.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == 'POST':
        form = request.form.to_dict()
        email = form['email']
        user = User.get_one(email=email)
        if user:
            # user.send_reset_email()
            print(form)
        return redirect(url_for('auth.login'))
    return render_template('reset_password.html', request=request, name="Reset Password")

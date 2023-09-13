from pywebio.platform.flask import webio_view
from flask import redirect, request, render_template_string
from flask_security import login_user
from flask import current_app as app # This is to access the app context
from admin.views.app_admin import admin_required
from models import User
from decorators import login_required_webio_view


@app.route('/login', methods=['GET', 'POST'])
@admin_required
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()  # Use hashed passwords in production
        if user.check_password(password):
            login_user(user)
            return redirect('/admin')
        else:
            return redirect('/login')
    return render_template_string("""
        <form method="post">
            Email: <input type="email" name="email"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    """)


@app.route('/dashboard')
@login_required_webio_view
def dashboard():
    return webio_view(app)


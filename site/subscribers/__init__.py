# subscribers/__init__.py
from .forms import SubscriberForm, LoginForm, UpdateForm
from .models import db, Subscriber, User, Role, SubscriberType, Tier
import bcrypt
import requests
from flask import render_template, redirect, url_for, flash, Blueprint, request, jsonify
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.routing import BuildError
subscribers = Blueprint('subscribers', __name__, template_folder="templates")


@subscribers.route('/register', methods=['GET', 'POST'])
def register():
    form = SubscriberForm()
    if form.validate_on_submit():
        # Check if the entered value is a valid SubscriberType enum member
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        sub = Subscriber(name=form.name.data,
                            is_active=True,
                            email=form.email.data,
                            password=hashed_password,
                            confirm_password=hashed_password,
                            address=form.address.data,
                            phone_number=form.phone_number.data,
                            billing_details=form.billing_details.data,
                            payment_method=form.payment_method.data)
        db.session.add(sub)
        db.session.commit()
        email_hash = bcrypt.hashpw(sub.email.encode('utf-8'), bcrypt.gensalt())
        sub.verify_code = email_hash
        # verify_url = f'http://127.0.0.1:8080/?subscriber={email_hash}'
        # return jsonify({"cherrypy_verify_url": verify_url})
        return redirect(url_for('subscribers.login'))
    return render_template('/register.html', form=form)


@subscribers.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('subscribers.dashboard'))
    if form.validate_on_submit():
        # Use filter_by to filter by email and use first() to get the first matching result
        subscriber = Subscriber.query.filter_by(email=form.email.data).first()
        if subscriber:
            email_hash = subscriber.email
            email_hash = bcrypt.hashpw(email_hash.encode('utf-8'), bcrypt.gensalt())
            if bcrypt.checkpw(form.password.data.encode('utf-8'), subscriber.password):
                if subscriber.verified is True:
                    login_user(subscriber)
                    return redirect(url_for('subscribers.dashboard'))
                # Send a verification email each time an unverified user attempts login
                subscriber.verify_code = email_hash
                db.session.commit()
                verify_url = f'http://127.0.0.1:8080/?subscriber={email_hash}'
                response = requests.get(verify_url)
                if response.status_code == 200:
                    flash(f'Verification email link and code sent to {form.email.data}')
                    flash('To resend verification email, try to login again')
            else:
                flash('Login unsuccessful. Please check email and password')
        else:
            flash('Email address not found. Please register.')
    return render_template('/login.html', form=form)


@subscribers.route('/confirm', methods=['GET', 'POST'])
def confirm(subscriber=None):
    user = Subscriber.query.filter_by(verify_code=subscriber).first()
    user.verified = True
    db.session.commit()
    # return jsonify({"user": user.email, "verified": user.verified})
    # Login Subscriber object
    login_user(user)
    if request.method == 'POST':
        return redirect(url_for('subscribers.dashboard'))
    return render_template('/login_confirmation_redirect.html')


@subscribers.route('/dashboard')
@login_required
def dashboard():
    try:
        return render_template('/dashboard.html')
    except BuildError:
        return redirect(url_for('subscribers.login'))


@subscribers.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('subscribers.login'))


@subscribers.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    form = UpdateForm()
    if form.validate_on_submit():
        # Check if the entered value is a valid SubscriberType enum member
        return redirect(url_for('subscribers.dashboard'))
    return render_template('/update.html', form=form)


@subscribers.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    account = Subscriber.query.filter_by(email=current_user.email).first()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('subscribers.register'))
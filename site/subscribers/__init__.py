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
        hash_email = bcrypt.hashpw(sub.email.encode('utf-8'), bcrypt.gensalt())
        sub.verify_code = hash_email
        db.session.commit()
        verify_url = f'http://127.0.0.1:8080/?subscriber={hash_email}'
        requests.get(verify_url)
        flash(f'Verification email link and code sent to {form.email.data}')
        # return jsonify({"cherrypy_verify_url": verify_url})
        return redirect(url_for('subscribers.login'))
    return render_template('/register.html', form=form)


@subscribers.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            flash('Login unsuccessful. Please check your information and try again.')
        try:
            subscriber = Subscriber.query.filter_by(email=form.email.data).first()
            if not bcrypt.checkpw(form.password.data.encode('utf-8'), subscriber.password):
                flash('Login unsuccessful. Please check password')
            if subscriber.verified is False:
                # Send a verification email each time an unverified user attempts login
                hash_email = subscriber.verify_code
                verify_url = f'http://127.0.0.1:8080/?subscriber={hash_email}'
                response = requests.get(verify_url)
                if response.status_code != 200:
                    flash(f'You must confirm your email address {form.email.data}.')
                flash(f'Verification link and code sent')
            else:
                login_user(subscriber)
        except AttributeError:
            flash('Email address not found. Please register.')
    if current_user.is_authenticated:
        return redirect(url_for('subscribers.dashboard'))
    return render_template('/login.html', form=form)


@subscribers.route('/confirm', methods=['GET', 'POST'])
def confirm(subscriber=None):
    user = Subscriber.query.filter_by(verify_code=subscriber).first()
    user.verified = True
    db.session.commit()
    # return jsonify({"user": user.email, "verified": user.verified})
    # Login Subscriber object
    # login_user(user)
    if request.method == 'POST':
        return redirect(url_for('subscribers.login'))
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
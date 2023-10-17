# subscribers/__init__.py
from .forms import SubscriberForm, LoginForm, UpdateForm
from .models import db, Subscriber, User, Role, SubscriberType, Tier
import bcrypt
from flask import render_template, redirect, url_for,flash, Blueprint, request
from flask_login import current_user, login_user, login_required, logout_user
subscribers = Blueprint('subscribers', __name__, template_folder="templates")


@subscribers.route('/register', methods=['GET', 'POST'])
def register():
    form = SubscriberForm()
    if form.validate_on_submit():
        # Check if the entered value is a valid SubscriberType enum member
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        sub = Subscriber(name=form.name.data,
                            email=form.email.data,
                            password=hashed_password,
                            confirm_password=hashed_password,
                            address=form.address.data,
                            phone_number=form.phone_number.data,
                            billing_details=form.billing_details.data,
                            payment_method=form.payment_method.data)
        db.session.add(sub)
        db.session.commit()
        flash('Check the email address provided in registration for confirmation link.')
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
            # Authentication logic (e.g., check password)
            if bcrypt.checkpw(form.password.data.encode('utf-8'), subscriber.password):
                login_user(subscriber)
                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect(url_for('subscribers.dashboard'))
            else:
                flash('Login unsuccessful. Please check email and password')
        else:
            flash('Email address not found. Please register.')
    return render_template('login.html', form=form)


@subscribers.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


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
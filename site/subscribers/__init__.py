# subscribers/__init__.py
from .forms import SubscriberForm, LoginForm
from .models import db, Subscriber, User, Role, SubscriberType, Tier
import bcrypt
from flask import render_template, redirect, url_for,flash, Blueprint, request
from flask_security import current_user, login_user, login_required


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
        flash('Check the email address provided in registration for confirmation link.', 'success')
        return redirect(url_for('subscribers.login'))
    else:
        flash('Registration unsuccessful.', 'danger')
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
                flash('Login successful!', 'success')
                # Log the user in (you might be missing this step)
                login_user(subscriber)
                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect(url_for('subscribers.dashboard'))
            else:
                flash('Login unsuccessful. Please check email and password', 'danger')
        else:
            flash('Email address not found. Please register.', 'danger')
    return render_template('login.html', form=form)


@login_required
@subscribers.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
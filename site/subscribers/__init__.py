# subscribers/__init__.py
from .forms import SubscriberForm, LoginForm
from .models import db, Subscriber, User, Role  # Import the db instance from models.py
import bcrypt
from flask import render_template, redirect, url_for,flash, Blueprint
from flask_security import current_user, login_required

subscribers = Blueprint('subscribers', __name__, template_folder="templates")


@subscribers.route('/register', methods=['GET', 'POST'])
def register():
    form = SubscriberForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        sub = Subscriber(name=form.name.data,
                            email=form.email.data,
                            password=hashed_password,
                            confirm_password=hashed_password,
                            subscriber_type=form.subscriber_type.data,
                            tier=form.tier.data,
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
        return redirect(url_for('dashboard'))
    if form.validate_on_submit():
        subscriber = Subscriber.query.filter_by(email=form.email.data).first()
        if subscriber and bcrypt.checkpw(form.password.data.encode('utf-8'), subscriber.password):
            flash('Login successful!', 'success')
            return redirect(url_for('subscribers.dashboard'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('/login.html', form=form)


@subscribers.route('/dashboard')
# @login_required
def dashboard():
    return render_template('dashboard.html')
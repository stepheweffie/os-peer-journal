from flask import render_template, redirect, url_for,flash, Blueprint
from models import db, Subscriber
from forms import SubscriberForm, UpdateSubscriberForm, LoginForm
import bcrypt
from flask_login import login_required, current_user


subscribers = Blueprint('subscribers', __name__)


@subscribers.route('/register', methods=['GET', 'POST'])
def register():
    form = SubscriberForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        subscriber = Subscriber(name=form.name.data, email=form.email.data, password=hashed_password,
                                subscriber_type=form.subscriber_type.data, tier=form.tier.data,
                                address=form.address.data, phone_number=form.phone_number.data,
                                billing_details=form.billing_details.data)
        db.session.add(subscriber)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('read_subscriber'))
    return render_template('register.html', form=form)


@subscribers.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if form.validate_on_submit():
        subscriber = Subscriber.query.filter_by(email=form.email.data).first()
        if subscriber and bcrypt.checkpw(form.password.data.encode('utf-8'), subscriber.password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)


@subscribers.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@subscribers.route('/<int:subscriber_id>')
def read_subscriber(subscriber_id):
    subscriber = Subscriber.query.get_or_404(subscriber_id)
    return render_template('subscriber.html', subscriber=subscriber)


@subscribers.route('/<int:subscriber_id>/update', methods=['GET', 'POST'])
@login_required
def update_subscriber(subscriber_id):
    subscriber = Subscriber.query.get_or_404(subscriber_id)
    form = UpdateSubscriberForm(obj=subscriber)
    if form.validate_on_submit():
        subscriber.name = form.name.data
        subscriber.email = form.email.data
        subscriber.subscriber_type = form.subscriber_type.data
        subscriber.tier = form.tier.data
        subscriber.address = form.address.data
        subscriber.phone_number = form.phone_number.data
        subscriber.billing_details = form.billing_details.data
        db.session.commit()
        flash('Subscriber details updated!', 'success')
        return redirect(url_for('dashboard', subscriber_id=subscriber.id))
    return render_template('update.html', form=form)


@subscribers.route('/<int:subscriber_id>/delete', methods=['POST'])
@login_required
def delete_subscriber(subscriber_id):
    subscriber = Subscriber.query.get_or_404(subscriber_id)
    db.session.delete(subscriber)
    db.session.commit()
    flash('Subscriber deleted!', 'success')
    return redirect(url_for('register'))

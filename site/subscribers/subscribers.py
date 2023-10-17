from flask import render_template, redirect, url_for,flash, Blueprint
from subscribers.forms import SubscriberForm, UpdateSubscriberForm, LoginForm
import bcrypt
from subscribers.models import Subscriber, db
from flask_security import login_required, current_user
from __init__ import subscribers



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

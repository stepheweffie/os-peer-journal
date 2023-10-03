from flask import Flask, render_template, redirect, url_for,flash
from models import db, Subscriber
from forms import SubscriberForm, UpdateSubscriberForm
import bcrypt

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = SubscriberForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        subscriber = Subscriber(name=form.name.data, email=form.email.data, password=hashed_password, subscriber_type=form.subscriber_type.data, tier=form.tier.data, address=form.address.data, phone_number=form.phone_number.data, billing_details=form.billing_details.data)
        db.session.add(subscriber)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/subscriber/<int:subscriber_id>')
def read_subscriber(subscriber_id):
    subscriber = Subscriber.query.get_or_404(subscriber_id)
    return render_template('subscriber.html', subscriber=subscriber)


@app.route('/subscriber/<int:subscriber_id>/update', methods=['GET', 'POST'])
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
        return redirect(url_for('subscriber', subscriber_id=subscriber.id))
    return render_template('subscriber.html', form=form)


@app.route('/subscriber/<int:subscriber_id>/delete', methods=['POST'])
def delete_subscriber(subscriber_id):
    subscriber = Subscriber.query.get_or_404(subscriber_id)
    db.session.delete(subscriber)
    db.session.commit()
    flash('Subscriber deleted!', 'success')
    return redirect(url_for('index'))

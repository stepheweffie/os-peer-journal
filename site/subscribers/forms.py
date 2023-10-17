from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from subscribers.models import SubscriberType, Tier


class SubscriberForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    address = StringField('Address')
    phone_number = StringField('Phone Number')
    billing_details = StringField('Billing Details')
    payment_method = StringField('Payment Method')
    submit = SubmitField('Register')


class UpdateForm(SubscriberForm):
    submit = SubmitField('Update')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')



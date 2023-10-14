from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from models import SubscriberType, Tier


class SubscriberForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    subscriber_type = SelectField('Subscriber Type', choices=[(type, type.value) for type in SubscriberType], validators=[DataRequired()])
    tier = SelectField('Tier', choices=[(tier, tier.value) for tier in Tier], validators=[DataRequired()])
    address = StringField('Address')
    phone_number = StringField('Phone Number')
    billing_details = StringField('Billing Details')
    submit = SubmitField('Register')


class UpdateSubscriberForm(SubscriberForm):
    submit = SubmitField('Update')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')



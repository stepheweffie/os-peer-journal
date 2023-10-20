from enum import Enum
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


class SubscriberType(Enum):
    college_library = "College Library"
    other_library = "Other Library"
    corporation = "Corporation"
    nonprofit = "Nonprofit"
    individual = "Individual"
    government = "Government Office or Agency"


class Tier(Enum):
    INDIVIDUAL = "Individual"
    EDUCATIONAL = "Educational"
    CORPORATE = "Corporate"
    NONPROFIT = "Nonprofit"
    GOVERNMENT = "Government"


class Subscriber(db.Model, UserMixin):
    __tablename__ = 'subscriber'
    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # Store hashed!
    confirm_password = db.Column(db.String(120), nullable=False)  # Store hashed!
    subscriber_type = db.Column(db.Enum(SubscriberType), nullable=True)
    tier = db.Column(db.Enum(Tier), nullable=True)  # Can be None if you want to set it later.
    verify_code = db.Column(db.String(8), nullable=True)
    verified = db.Column(db.Boolean, default=False)
    # Billing, contact info, etc.
    address = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
    billing_details = db.Column(db.String(300))  # Depending on your requirement, this might need to be more complex.
    payment_method = db.Column(db.String(100))  # Depending on your requirement, this might need to be more complex.
    contact_person = db.Column(db.String(100), nullable=True)  # Can be None if you want to set it later.


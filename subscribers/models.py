# shared_db/models.py
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()


class SubscriberType(Enum):
    COLLEGE_LIBRARY = "College Library"
    CORPORATION = "Corporation"
    NONPROFIT = "Nonprofit"
    INDIVIDUAL = "Individual"  # Add this if you want to consider individual subscribers as well.


class Tier(Enum):
    BASIC = "Basic"
    PREMIUM = "Premium"
    ENTERPRISE = "Enterprise"
    # Add more tiers if necessary.


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # Store hashed!
    subscriber_type = db.Column(db.Enum(SubscriberType), nullable=False)
    tier = db.Column(db.Enum(Tier), nullable=True)  # Can be None if you want to set it later.

    # Billing, contact info, etc.
    address = db.Column(db.String(200))
    phone_number = db.Column(db.String(20))
    billing_details = db.Column(db.String(300))  # Depending on your requirement, this might need to be more complex.
    contact_person = db.Column(db.String(100))


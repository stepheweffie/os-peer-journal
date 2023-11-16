from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin
from flask_bcrypt import Bcrypt
import uuid
from flask_security import SQLAlchemyUserDatastore
from flask_marshmallow import Marshmallow, Schema
import datetime
db = SQLAlchemy()
bcrypt = Bcrypt()
ma = Marshmallow()
# Create database connection object

roles_users = db.Table(
    'roles_users',
    db.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),  # Assuming your user table is named 'users'
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(150), nullable=True)
    last_name = db.Column(db.String(150), nullable=True)
    password = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    date_created = db.Column(db.DateTime())
    password_hash = db.Column(db.String(128))
    verified = db.Column(db.Boolean(), default=False)
    fs_uniquifier = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    papers = db.relationship('Paper', back_populates='user')
    roles = db.relationship('Role',
                            secondary='roles_users',
                            backref=db.backref('users',
                                               lazy='dynamic'))

    def set_password(self, naked_password):
        self.password_hash = bcrypt.generate_password_hash(naked_password).decode('utf-8')
        self.password = self.password_hash

    def check_password(self, hashed_password):
        return bcrypt.check_password_hash(self.password_hash, hashed_password)

    def reset_password(self, email, new_password):
        reset_user = self.get_one(email)
        if reset_user:
            self.set_password(new_password)
            if self.check_password(new_password):
                db.session.commit()
                print(f"Password for user email {email} has been reset.")
        else:
            print(f"No user found with email {email}.")

    def delete(self, email):
        user = self.get_one(email)
        if user:
            if user.check_password(user.password):
                db.session.delete(user)
                db.session.commit()
                return f"User with username {email} deleted."
        else:
            return f"No user found with username {email}."

    def serialize(self):
        return {
            'id': self.id,
            'is_admin': self.is_admin,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'authenticated': self.authenticated,
            'papers': self.papers,
            'date_created': self.date_created
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_one(email):
        return User.query.filter_by(email=email).first()

    # Without the following properties, the flask_security module will not work properly.
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False


class Paper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    authors = db.Column(db.String(255), nullable=False)
    abstract = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    file = db.Column(db.String(255), nullable=False)
    under_review = db.Column(db.Boolean, default=True)
    reviewer = db.Column(db.String(255), nullable=True)
    published = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='papers')


class UserSchema(Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'is_active', 'date_created')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % self.name


user_datastore = SQLAlchemyUserDatastore(db, User, Role)

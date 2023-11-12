from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin
from flask_bcrypt import Bcrypt
import uuid
from flask_security import SQLAlchemyUserDatastore
from flask_marshmallow import Marshmallow, Schema

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
    username = db.Column(db.String(150), unique=True, nullable=True)
    password = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    confirmed_at = db.Column(db.DateTime())
    password_hash = db.Column(db.String(128))
    active = db.Column(db.Boolean())
    authenticated = db.Column(db.Boolean(), default=False)
    # papers = db.relationship('PublishedPapers', backref='title', lazy=True)
    fs_uniquifier = db.Column(db.String(36), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    roles = db.relationship('Role',
                            secondary='roles_users',
                            backref=db.backref('users',
                                               lazy='dynamic'))

    def set_password(self, naked_password):
        self.password_hash = bcrypt.generate_password_hash(naked_password).decode('utf-8')
        self.password = self.password_hash

    def check_password(self, hashed_password):
        return bcrypt.check_password_hash(self.password_hash, hashed_password)

    def reset_password(self, username, new_password):
        reset_user = self.query.filter_by(username=username).first()
        if reset_user:
            self.set_password(new_password)
            if self.check_password(new_password):
                db.session.commit()
                print(f"Password for user {username} has been reset.")
        else:
            print(f"No user found with username {username}.")

    def delete(self, username):
        user = self.query.filter_by(username=username).first()
        if user:
            if user.check_password(user.password):
                db.session.delete(user)
                db.session.commit()
                return f"User with username {username} deleted."
        else:
            return f"No user found with username {username}."

    def serialize(self):
        return {
            'id': self.id,
            'is_admin': self.is_admin,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'active': self.active,
            'authenticated': self.authenticated,
            # 'papers': self.papers,
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


class UserSchema(Schema):
    class Meta:
        fields = ('id', 'is_admin', 'first_name', 'last_name', 'email', 'date_created')


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

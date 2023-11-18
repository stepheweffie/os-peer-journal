from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os
import os.path as op
from flask_wtf.csrf import CSRFProtect
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER = '../instance/user.db'
UPLOAD_FOLDER = 'papers'  # change this to your desired upload folder
ALLOWED_EXTENSIONS = {'pdf', 'ipynb'}
db = SQLAlchemy()
ma = Marshmallow()


class PublishedPapers(db.Model):
    __tablename__ = 'published_papers'
    __bind_key__ = 'publishedpapers'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    authors = db.Column(db.String(200), nullable=False)
    abstract = db.Column(db.Text, nullable=False)
    file = db.Column(db.LargeBinary, nullable=False)  # The actual file
    filepath = db.Column(db.String(200), nullable=True)  # Path to where the file is saved
    filename = db.Column(db.String(200), nullable=True)  # Name of the file
    reviewed = db.Column(db.Boolean, default=False, nullable=True)  # Whether the paper has been reviewed or not
    reviewed_by = db.Column(db.String(200), nullable=True)  # The reviewer's name
    review_date = db.Column(db.String(200), nullable=True)  # The date of review
    review_data = db.Column(db.Text, nullable=True)  # The review itself
    pub_date = db.Column(db.String(200), nullable=True)  # Date of publication
    published_by = db.Column(db.String(200), nullable=True)  # The publisher's name
    published = db.Column(db.Boolean, default=False, nullable=True)  # Whether the paper has been published or not


class Review(db.Model):
    __tablename__ = 'reviews'
    __bind_key__ = 'publishedpapers'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    authors = db.Column(db.String(200), nullable=False)
    filename = db.Column(db.String(200), nullable=True)  # Name of the file
    reviewed_by = db.Column(db.String(200), nullable=True)  # The reviewer's name
    review_date = db.Column(db.String(200), nullable=True)  # The date of review
    review = db.Column(db.Text, nullable=True)  # The review itself
    fail = db.Column(db.Boolean, default=False, nullable=True)  # Whether the paper has been reviewed or not


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///publishedpapers.db'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'publishedpapers': 'sqlite:///publishedpapers.db',
        'users': f'sqlite:///{os.path.join(BASE_DIR, USER)}'
    }
    CSRFProtect(app)
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        import routes
        # db.drop_all()
        Migrate(app, db)
        db.create_all()
    return app


if __name__ == '__main__':
    file_path = op.join(op.dirname(__file__), 'papers')
    try:
        os.mkdir(file_path)
    except OSError:
        pass
    app = create_app()
    app.run()





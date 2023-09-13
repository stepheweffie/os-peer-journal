from flask import Flask
from flask_restful import Api
api = Api()
UPLOAD_FOLDER = 'papers'  # change this to your desired upload folder
ALLOWED_EXTENSIONS = {'pdf', 'ipynb'}
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class PublishedPapers(db.Model):
    __bind_key__ = 'publishedpapers'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    abstract = db.Column(db.Text, nullable=False)
    authors = db.Column(db.String(200), nullable=False)
    filepath = db.Column(db.String(200), nullable=False)  # Path to where the file is saved
    filename = db.Column(db.String(200), nullable=False)  # Name of the file
    date = db.Column(db.String(200), nullable=False)  # Date of publication
    file = db.Column(db.LargeBinary, nullable=False)  # The actual file


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///publishedpapers.db'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'publishedpapers': 'sqlite:///publishedpapers.db',
    }

    db.init_app(app)
    api.init_app(app)
    from views import initialize_routes
    initialize_routes(api)
    with app.app_context():
        import views
        # db.drop_all()
        db.create_all()
        # papers = PublishedPapers.query.all()
        # print(papers)
    return app





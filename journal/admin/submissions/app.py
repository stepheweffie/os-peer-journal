from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_marshmallow import Marshmallow, Schema


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
    reviewed_date = db.Column(db.String(200), nullable=True)  # The date of review
    review_data = db.Column(db.Text, nullable=True)  # The review data
    pub_date = db.Column(db.String(200), nullable=True)  # Date of publication
    published_by = db.Column(db.String(200), nullable=True)  # The publisher's name
    published = db.Column(db.Boolean, default=False, nullable=True)  # Whether the paper has been published or not


class ReviewPaperSchema(Schema):
    class Meta:
        fields = ('title', 'authors', 'abstract', 'reviewed', 'reviewed_by', 'reviewed_date', 'review_data', 'filename')


paper_schema = ReviewPaperSchema()
papers_schema = ReviewPaperSchema(many=True)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///publishedpapers.db'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'publishedpapers': 'sqlite:///publishedpapers.db',
    }
    db.init_app(app)
    ma.init_app(app)

    try:
        with app.app_context():
            import routes
            # db.drop_all()
            db.create_all()
    except Exception as e:
        logging.error(f"Error during app initialization: {str(e)}")
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()





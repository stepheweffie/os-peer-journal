
'''
Published submissions to publishedpapers.db go into the api reference.
Journal entries are published to the front page of the journal, styled with links, and part of
the readable presentation content.
'''
from flask import Flask


def create_app():
    app = Flask(__name__)
    with app.app_context():
        from .routes import journal
        app.register_blueprint(journal, url_prefix='/journal')
        return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


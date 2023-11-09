from flask import Flask


def create_app():
    app = Flask(__name__)
    from routes import journal
    app.register_blueprint(journal, url_prefix='/journal')
    return app



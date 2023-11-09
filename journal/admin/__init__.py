from flask import Flask
import os
from flask_security import Security
from dotenv import load_dotenv
import sys
from config import UPLOAD_FOLDER, BASE_DIR, TARGET_DIR, ALLOWED_EXTENSIONS, PARENT_DIR
from views import *
load_dotenv()

app = Flask(__name__)

app.config.from_object('config')
app.secret_key = os.getenv('SECRET_KEY')
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
salt = os.urandom(16).hex()
app.config['SECURITY_PASSWORD_SALT'] = salt
app.config['ADMIN_EMAIL'] = os.getenv('ADMIN_EMAIL')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
DB = os.getenv('DB')
PAPERS = os.getenv('PAPERS')
# from pywebio import STATIC_PATH
PAPERS_DB = '../submissions/instance/publishedpapers.db'
API_MODEL_DIR = '../api'
sys.path.append(PARENT_DIR)


if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)


app.config['SQLALCHEMY_BINDS'] = {
    'users': f'sqlite:///{BASE_DIR}/{DB}',
    'publishedpapers': f'sqlite:///{PARENT_DIR}/{PAPERS}'
}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PAPERS_DB'] = PAPERS_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SERVER_NAME'] = '127.0.0.1:5000'
app.config['PREFERRED_URL_SCHEME'] = os.getenv('PREFERRED_URL_SCHEME')

with app.app_context():
    from models import db, bcrypt, user_datastore
    from views.pywebio_logic import pywebio_logic_blueprint
    from views.app_admin import admin_blueprint
    db.init_app(app)
    db.create_all()
    db.session.commit()
    bcrypt.init_app(app)
    security = Security(app, user_datastore)
    app.register_blueprint(pywebio_logic_blueprint)
    app.register_blueprint(admin_blueprint)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

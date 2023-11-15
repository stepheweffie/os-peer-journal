import os
from dotenv import load_dotenv
load_dotenv()
PAPERS = os.getenv('PAPERS')
DB = os.getenv('DB')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
UPLOAD_FOLDER = 'submissions/papers'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(BASE_DIR, UPLOAD_FOLDER)
PARENT_DIR = os.path.dirname(BASE_DIR)
ALLOWED_EXTENSIONS = {'pdf', 'ipynb'}
SECRET_KEY = 'secret_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'
FLASK_DEBUG = True

SQLALCHEMY_BINDS = {
    'users': f'sqlite:///{os.path.join(BASE_DIR, DB)}',
    'publishedpapers': f'sqlite:///{os.path.join(BASE_DIR, PAPERS)}'
}

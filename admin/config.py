import os

UPLOAD_FOLDER = '../api/papers'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(BASE_DIR, UPLOAD_FOLDER)
PARENT_DIR = os.path.dirname(BASE_DIR)
ALLOWED_EXTENSIONS = {'pdf', 'ipynb'}
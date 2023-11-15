import os
import os.path as op
import shutil

allowed = ['pdf', 'ipynb']


def copy_papers(paper):
    file_type = paper.split('.')[-1]
    if file_type not in allowed:
        return False
    _directory_path = op.join(op.dirname(__file__), f'static/uploads/{file_type}')
    if not op.exists(_directory_path):
        os.makedirs(_directory_path)
    shutil.copy(paper, op.join(op.dirname(__file__), f'static/uploads/{file_type}'))
    return True

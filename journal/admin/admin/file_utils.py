import os
import os.path as op
import shutil

allowed = ['pdf', 'ipynb']


def copy_papers(paper):
    file_type = paper.filename.split('.')[-1]
    if file_type not in allowed:
        return False
    _directory_path = op.join(op.dirname(__file__), f'submissions/papers/uploads/{file_type}')
    if not op.exists(_directory_path):
        os.makedirs(_directory_path)
    shutil.copy(paper.filename, _directory_path)
    return True

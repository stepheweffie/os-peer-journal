from flask_restful import Resource, reqparse
from flask import request
from werkzeug.utils import secure_filename
import os
from flask import render_template
from __init__ import UPLOAD_FOLDER, db, PublishedPapers
from flask import current_app as app


task_parser = reqparse.RequestParser()
task_parser.add_argument('title', required=True, help="Title cannot be blank!")


class PaperUploadResource(Resource):
    def post(self):
        data = request.form
        title = data['title']
        abstract = data['abstract']
        authors = data['authors']

        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        paper = PublishedPapers(title=title, abstract=abstract, authors=authors, filepath=filepath)
        db.session.add(paper)
        db.session.commit()

        return {"message": "Paper uploaded and saved successfully"}, 201


class TaskListPapers(Resource):
    def get(self):
        tasks = PublishedPapers.query.all()
        return [{'id': task.id, 'title': task.title} for task in tasks]

    def post(self):
        args = task_parser.parse_args()
        task = PublishedPapers(title=args['title'])
        db.session.add(task)
        db.session.commit()
        return {'id': task.id, 'title': task.title}, 201


class TaskPapers(Resource):
    def get(self, task_id):
        task = PublishedPapers.query.get_or_404(task_id)
        return {'id': task.id, 'title': task.title}

    def put(self, task_id):
        args = task_parser.parse_args()
        task = PublishedPapers.query.get_or_404(task_id)
        task.title = args['title']
        db.session.commit()
        return {'id': task.id, 'title': task.title}

    def delete(self, task_id):
        task = PublishedPapers.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204


def initialize_routes(api):
    api.add_resource(PaperUploadResource, '/upload_paper')
    api.add_resource(TaskListPapers, '/papers')
    api.add_resource(TaskPapers, '/papers/<int:task_id>')


@app.route('/submit_paper', methods=['GET'])
def submit_paper():
    return render_template('submit_paper.html')
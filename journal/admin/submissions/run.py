from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
import datetime
app = Flask(__name__)
api = Api(app)
upload_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

paper_fields = {'title': fields.String,
                'abstract': fields.String,
                'authors': fields.String,
                'filepath': fields.String,
                'filename': fields.String,
                'date': fields.DateTime(dt_format='rfc822')}

PAPERS = {
    'paper1': {'title': 'build an API',
               'abstract': 'profit!',
               'authors': 'me',
               'filepath': 'papers',
               'filename': 'paper1',
               'date': f'{upload_date}'},
    'paper2': {'title': '?????'},
    'paper3': {'title': 'profit!'},
}


def abort_if_todo_doesnt_exist(paper_id):
    if paper_id not in PAPERS:
        abort(404, message="Paper {} doesn't exist".format(paper_id))


parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('abstract')
parser.add_argument('authors')
parser.add_argument('filepath')
parser.add_argument('filename')
parser.add_argument('date')


class PaperTask(Resource):
    def get(self, paper_id):
        abort_if_todo_doesnt_exist(paper_id)
        return PAPERS[paper_id]

    def delete(self, paper_id):
        abort_if_todo_doesnt_exist(paper_id)
        del PAPERS[paper_id]
        return '', 204

    def put(self, paper_id):
        args = parser.parse_args()
        title = args['title']
        PAPERS[paper_id]['title'] = title
        return title, 201


class PaperList(Resource):
    def get(self):
        return PAPERS

    def post(self):
        args = parser.parse_args()
        paper_id = int(max(PAPERS.keys()).lstrip('paper')) + 1
        paper_id = f'paper{paper_id}'
        PAPERS[paper_id] = {'title': args['title'],
                            'abstract': args['abstract'],
                            'authors': args['authors'],
                            'filepath': args['filepath'],
                            'filename': args['filename'],
                            'date': args['date']}
        return PAPERS[paper_id], 201


api.add_resource(PaperList, '/papers')
api.add_resource(PaperTask, '/paper/<paper_id>')


if __name__ == '__main__':
    app.run(debug=True)
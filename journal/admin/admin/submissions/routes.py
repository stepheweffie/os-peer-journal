from flask import request, url_for, redirect, render_template
from app import db, PublishedPapers
from flask import current_app as app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import datetime
from schemas import published_papers_schema, submitted_papers_schema, reviewed_papers_schema


class PublishPaperForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    file = FileField('File', validators=[FileRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return redirect(url_for('publish_paper'))


@app.route('/publish_paper', methods=['GET', 'POST'])
def publish_paper():
    form = PublishPaperForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = request.form['title']
            paper = PublishedPapers.query.filter_by(title=title).first()
            paper.file = request.files['file']
            paper.published = True
            paper.pub_date = datetime.datetime.now()
            db.session.add(paper)
            db.session.commit()
            return redirect(url_for('success_page'))
    return render_template('papers.html', form=form)


@app.route('/success_page', methods=['GET'])
def success_page():
    success = '''
    <h1>Success!</h1>
    '''
    return success


@app.route("/submitted_papers")
def submitted_papers():
    all_papers = PublishedPapers.query.filter_by(reviewed=False).all()
    result = submitted_papers_schema.dump(all_papers)
    return {'submitted_papers': result}


@app.route("/published_papers")
def published_papers():
    all_papers = PublishedPapers.query.filter_by(published=True).all()
    result = published_papers_schema.dump(all_papers)
    return {'published_papers': result}


@app.route("/reviewed_papers")
def submitted_papers():
    all_papers = PublishedPapers.query.filter_by(reviewed=True).all()
    result = reviewed_papers_schema.dump(all_papers)
    return {'reviewed_papers': result}

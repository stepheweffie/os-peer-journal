from flask import request, url_for, redirect, render_template
from app import db, PublishedPapers
from flask import current_app as app
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
import datetime
import os


class PublishPaperForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    abstract = TextAreaField('Abstract', validators=[DataRequired()])
    authors = StringField('Authors', validators=[DataRequired()])
    file = FileField('File', validators=[FileRequired()])


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
            paper.abstract = request.form['abstract']
            paper.authors = request.form['authors']
            paper.file = request.files['file'].read()
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


@app.route("/api/unreviewed_papers")
def papers():
    pdf_papers = os.listdir('papers/pdf')
    ipynb_papers = os.listdir('papers/notebooks')
    titles = pdf_papers + ipynb_papers
    return {"unreviewed_papers": titles}

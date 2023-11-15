
'''
Published submissions to publishedpapers.db
Journal entries are published to the front page of the journal, styled with links, and part of
the readable presentation content.
'''

import dash
from dash import html, Input, Output
from dotenv import load_dotenv
import dash_bootstrap_components as dbc
from flask import Flask
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from admin.submissions.app import PublishedPapers  # Import the model

server = Flask(__name__)
Base = declarative_base()
server.secret_key = 'secret_key'
server.config['SESSION_TYPE'] = 'filesystem'
Session(server)
load_dotenv()
engine = create_engine('sqlite:///admin/submissions/instance/publishedpapers.db', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


app = dash.Dash(external_stylesheets=[dbc.themes.MORPH],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
                server=server, suppress_callback_exceptions=True,
                use_pages=True,
                url_base_pathname='/journal/')

MAIN = html.Div(id='display-url-info')

app.layout = html.Div([
    html.H1('Published Papers'),
    dbc.Card(id='published-papers-container'),
    dbc.Pagination(id='pagination', max_value=8),
])


@app.callback(
    Output('published-papers-container', 'children'),
    Output('pagination', 'total_pages'),
    Input('pagination', 'page_current')
)
def display_published_papers(page):
    if page is None:  # Add this check
        page = 1  # Set a default value for page if it's None

    papers_per_page = 30
    start_idx = (page - 1) * papers_per_page
    end_idx = start_idx + papers_per_page
    papers = get_published_papers()

    total_pages = (len(papers) + papers_per_page - 1) // papers_per_page

    paper_cards = []
    for paper in papers[start_idx:end_idx]:
        card = dbc.Card([
            dbc.CardBody([
                html.H4(paper.title, className="card-title"),
                html.P(paper.author, className="card-text"),
                html.P(paper.abstract, className="card-text"),
            ])
        ])
        paper_cards.append(card)
    return paper_cards, total_pages


def get_published_papers():
    # Implement your database query to retrieve published papers here
    session = SessionLocal()
    papers = session.query(PublishedPapers).all()
    session.close()
    return papers


@app.callback(
    Output("published-papers", "children"),
    Input("pagination", "page_current"),
)
def update_published_papers(page):
    papers = get_published_papers()
    papers_per_page = 30
    total_pages = (len(papers) + papers_per_page - 1) // papers_per_page
    return display_published_papers(page), total_pages


if __name__ == "__main__":
    app.run_server(debug=True)


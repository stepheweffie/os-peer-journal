
'''
Published submissions to publishedpapers.db go into the api reference.
Journal entries are published to the front page of the journal, styled with links, and part of
the readable presentation content.
'''

import dash
from dash import html
from dotenv import load_dotenv
import dash_bootstrap_components as dbc
from flask import Flask
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
server = Flask(__name__)
Base = declarative_base()
server.secret_key = 'secret_key'
server.config['SESSION_TYPE'] = 'filesystem'
Session(server)
load_dotenv()
DATABASE_URL = "sqlite:///./sessions.db"  # Adjust as per your database
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)


app = dash.Dash(external_stylesheets=[dbc.themes.VAPOR],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
                server=server, suppress_callback_exceptions=True)
MAIN = html.Div(id='display-url-info')


app.layout = html.Div([
    html.Center(html.H1('Journal Front Page')),
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-10 col-xl-10", style={'max-width': '100%'})


if __name__ == "__main__":
    app.run_server(debug=True)


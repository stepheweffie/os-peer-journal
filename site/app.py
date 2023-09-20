import dash
from dash import html
from dash.dependencies import Input, Output, State
from dotenv import load_dotenv
import dash_bootstrap_components as dbc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_utils import add_email, add_contact
from models import Base
# import os
from templates.dash_body import BODY
from templates.dash_navbar import NAVBAR
from templates.pages import READ
from flask import Flask, session
from flask_session import Session
import dash_core_components as dcc

# Flask & Session Setup
server = Flask(__name__)
server.secret_key = 'supersecretkey'
server.config['SESSION_TYPE'] = 'filesystem'
Session(server)

# from templates.dash_nav import NAV
# from templates.dash_footer import FOOTER
load_dotenv()

# url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json'
# api_key = 'api_key=' + os.getenv('API_KEY')

DATABASE_URL = "sqlite:///./leads.db"  # Adjust as per your database
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)


app = dash.Dash(external_stylesheets=[dbc.themes.VAPOR], server=server, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url'),
    NAVBAR,
    html.Div(id='display-url-info'),
])

paths = dict()

paths['/'] = BODY
paths['/read'] = READ
paths['/subscribe'] = 'subscribe_layout'
paths['/about'] = 'about_layout'
paths['/people'] = 'people_layout'
paths['/contact'] = 'contact_layout'
paths['/faq'] = 'faq_layout'
paths['/terms'] = 'terms_layout'
paths['/privacy'] = 'privacy_layout'
# pages that rely on other modules
paths['/login'] = 'page_login'
paths['/logout'] = 'page_logout'
paths['/register'] = 'page_register'
paths['/dashboard'] = 'page_dashboard'
paths['/dashboard/leads'] = 'page_leads'
paths['/dashboard/leads/add'] = 'page_add_lead'
paths['/dashboard/leads/edit'] = 'page_edit_lead'


@app.callback(
    Output('display-url-info', 'children'),
    [Input('url', 'href'),
     Input('url', 'pathname')]
)
def display_url(href, pathname):
    if pathname in paths:
        return paths[pathname]
    return [
        html.P(f"Full URL (href): {href}"),
        html.P(f"Pathname: {pathname}")
    ]


@app.callback(
    Output("us-map", "figure"),
    Input("us-map", "relayoutData")
)
@app.callback(
    Output("email-output", "children"),
    Input("email-button", "n_clicks"),
    State("email-updates-input", "value"),
    prevent_initial_call=True
)
def process_email_form(n_clicks, email):
    if not email:
        return {}
    error_message = add_email(address=email)
    if error_message:
        return f"Error: {error_message}"
    # Return a style that hides the container
    session['form_submitted'] = True
    return {"display": "none"}


@app.callback(
    Output("contact-output", "children"),
    Input("contact-button", "n_clicks"),
    State("name-input", "value"),
    State("last-name-input", "value"),
    State('institution-input', 'value'),
    State("contact-email-input", "value"),
    State("phone-input", "value"),
    prevent_initial_call=True
)
def process_contact_form(n_clicks, first_name, last_name, institution, email, phone):
    if not (first_name and last_name and institution and email and phone):
        return "Please complete all fields."
    error_message = add_contact(first_name=first_name, last_name=last_name, institution=institution,
                                email=email, phone=phone)
    if error_message:
        return f"Error: {error_message}"
    return f"Thank you, {first_name}! We'll be in touch."


@app.callback(
    [Output("cookie-consent-offcanvas", "is_open"),
     Output("cookie-consent-offcanvas", "backdrop")],
    [Input("accept-button", "n_clicks"),
     Input("reject-button", "n_clicks")],
    prevent_initial_call=True
)
def toggle_offcanvas(accept_clicks, reject_clicks):
    # Close the offcanvas regardless of the button clicked
    # Here, you can set a session variable to remember the user's choice
    if accept_clicks:
        session['cookies_accepted'] = True
    else:
        session['cookies_accepted'] = False
    return False, False


if __name__ == "__main__":
    app.run_server(debug=True)


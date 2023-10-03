import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dotenv import load_dotenv
import dash_bootstrap_components as dbc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_utils import add_email, add_contact
from models import Base
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
from pages.dash_body import BODY
from pages.dash_navbar import NAVBAR
from pages.dash_read import READ
from pages.dash_subscribe import SUBSCRIBE
from pages.dash_about import ABOUT
from pages.dash_people import PEOPLE
from pages.dash_contact import CONTACT
from pages.dash_faq import FAQ
from pages.dash_terms import TERMS
from pages.dash_privacy import PRIVACY
from flask import Flask, session
from flask_session import Session

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


app = dash.Dash(external_stylesheets=[dbc.themes.VAPOR],
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
                server=server, suppress_callback_exceptions=True)
MAIN = html.Div(id='display-url-info')

app.layout = html.Div([
    dcc.Location(id='url'),
    # HEAD,
    NAVBAR,
    MAIN,
    # FOOTER,
])
paths = dict()
paths['/'] = BODY
paths['/read'] = READ
paths['/subscribe'] = SUBSCRIBE
paths['/about'] = ABOUT
paths['/people'] = PEOPLE
paths['/contact'] = CONTACT
paths['/faq'] = FAQ
paths['/terms'] = TERMS
paths['/privacy'] = PRIVACY
# outside app module
paths['/login'] = 'page_login'
paths['/logout'] = 'page_logout'
paths['/register/<token>'] = 'page_register'
paths['/reset-password'] = 'page_reset_password'
paths['/reset-password/<token>'] = 'page_reset_password_token'
paths['/verify-email'] = 'page_verify_email'
paths['/verify-email/<token>'] = 'page_verify_email_token'
paths['/verify-email/<token>/<email>'] = 'page_verify_email_token_email'
paths['/callback'] = 'page_callback'
paths['/callback/email'] = 'page_callback_email'

paths['/profile'] = 'page_profile'
paths['/profile/edit'] = 'page_edit_profile'
paths['/profile/change-password'] = 'page_change_password'
paths['/profile/change-email'] = 'page_change_email'
paths['/profile/change-email/<token>'] = 'page_change_email_token'
paths['/profile/delete'] = 'page_delete_profile'
paths['/profile/delete/<token>'] = 'page_delete_profile_token'
paths['/profile/confirm'] = 'page_confirm_profile'
paths['/profile/confirm/<token>'] = 'page_confirm_profile_token'
paths['/profile/confirm/<token>/<email>'] = 'page_confirm_profile_token_email'
paths['/profile/confirm/<token>/<email>/<password>'] = 'page_confirm_profile_token_email_password'

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


# Define callback to toggle the collapse
@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")]
)
def toggle_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# Define callback to manage form submission (Optional, based on your needs)

@app.callback(
    Output("contact-output", "children"),
    [Input("contact-button", "n_clicks")],
    [State("name-input", "value"),
     State("last-name-input", "value"),
     State("institution-input", "value"),
     State("phone-input", "value"),
     State("contact-email-input", "value")]
)
def submit_form(n_clicks, name, last_name, institution, phone, email):
    if n_clicks:
        # Here you can manage the form data, e.g., store it in a database or send an email
        return html.P(f"Thank you {name} {last_name} for your submission from {institution}. We will contact you shortly at {email} or {phone}.")
    return ""


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


@app.callback(
    Output('animated-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph(n):
    x = np.linspace(0, 10, 100)
    waves = [
        np.sin(x * freq + n / 10.0)
        for freq in np.linspace(1, 2, 5)
    ]
    # Vapor theme colors
    vapor_colors = [
        "#7c4dff",
        "#6610f2",
        "#6f42c1",
        "#00ffff",
        "#76ff03",
    ]

    # Creating traces for each wave
    traces = [
        go.Scatter(
            x=x, y=wave,
            mode='lines',
            line=dict(width=2, color=color),
        )
        for wave, color in zip(waves, vapor_colors)
    ]

    # Updating the figure layout
    layout = go.Layout(
        showlegend=False,
        xaxis=dict(
            showline=False,
            showgrid=False,
            zeroline=False,
            showticklabels=False,  # Remove tick labels
            title_text='',  # Ensure no axis title is displayed
        ),
        yaxis=dict(
            showline=False,
            showgrid=False,
            zeroline=False,
            showticklabels=False,  # Remove tick labels
            title_text='',  # Ensure no axis title is displayed
        ),
        margin=dict(t=20, r=20, l=20, b=20),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )

    return {'data': traces, 'layout': layout}


if __name__ == "__main__":
    app.run_server(debug=True)


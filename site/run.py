import dash
from dash import html, dcc
from dotenv import load_dotenv
import dash_bootstrap_components as dbc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import numpy as np
from pages.dash_cover import COVER
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
from pages.dash_footer import FOOTER
from flask import Flask, session
from flask_session import Session
import re
from db_utils import add_user_contact, add_email_subscription, add_sales_contact

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
    #MAINNAV
    NAVBAR,
    dbc.Container([
        MAIN,
        FOOTER,
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-10 col-xl-10", style={'max-width': '100%'}),

])
paths = dict()
paths['/'] = COVER
paths['/explore'] = BODY
paths['/read'] = READ
paths['/subscribe'] = SUBSCRIBE
paths['/about'] = ABOUT
paths['/people'] = PEOPLE
paths['/contact'] = CONTACT
paths['/faq'] = FAQ
paths['/terms'] = TERMS
paths['/privacy'] = PRIVACY
# subscribers app module
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
# blog app module
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
# coffers app module
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

# @app.callback(

# )


@app.callback(
    [Output("email-input", "valid"), Output("email-input", "invalid")],
    [Input("email-input", "value")],
)
def check_validity(text):
    email = ''
    endings = ['edu', 'com', 'org']
    if text:
        if text.count("@") == 1:
            if '@.' in text:
                return False, True
            for ending in endings:
                ending = '.' + ending
                if text.endswith(ending):
                    email = True
                    session['email'] = text
            return email, not email
        if text.count("@") > 1:
            return False, True
        if text.count("@") == 0:
            return False, True
    return False, False


@app.callback(
              Output("invalid-info-alert", "is_open"),
              Output("check-email-alert", "is_open"),
              [Input("email-updates-button", "n_clicks")],
              [State("email-input", "value"),
               State("username-updates-input", "value")],
)
def on_button_click(click, email, name):
    email_pattern = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if click:
        if not name or not email:
            return True, False
        if not re.match(email_pattern, email):
            return True, False
        add_email_subscription(name, email)
        # email sending logic here
        return False, True
    return False, False


@app.callback(
    Output("subscribe-collapse", "is_open"),
    [Input("subscribe-collapse-button", "n_clicks")],
    [State("subscribe-collapse", "is_open")],
)
def toggle_collapse(n_clicks, is_open):
    if n_clicks > 0:
        return not is_open
    return is_open


@app.callback(
    [Output("collapse-info-alert", "is_open"),
     Output("collapse-success-alert", "is_open"),
     Output("collapse-phone-alert", "is_open"),
     Output("collapse-email-alert", "is_open"),
     Output("subscribe-contact-output", "children")],
    [Input("subscribe-contact-button", "n_clicks")],
    [State("name-input", "value"),
     State("last-name-input", "value"),
     State("institution-input", "value"),
     State("phone-input", "value"),
     State("contact-email-input", "value"),
     State("subscribe-contact-message", "value")]
)
def submit_form(n_clicks, name, last_name, institution, phone, email, message):
    phone_pattern = '^(\d{10}|(\(\d{3}\)\s?\d{3}-\d{4})|\d{3}-\d{3}-\d{4})$'
    email_pattern = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if n_clicks > 0:
        if not re.match(phone_pattern, phone):
            return False, False, True, False, ""
        if not re.match(email_pattern, email):
            return False, False, False, True, ""
        if not all([name, last_name, institution, phone, email, message]):  # Check all fields are filled
            return True, False, False, False, ""
        else:
            add_sales_contact(first_name=name, last_name=last_name, institution=institution, email=email, phone=phone)
            # [Your Email Sending Logic Here]
            # Close the alert and display email verification message
            return False, True, False, False, ""
    return False, False, False, False, ""


@app.callback(
    [Output("modal", "is_open"), Output("verify-modal", "is_open")],
    [Input("open-modal", "n_clicks"), Input("close-modal", "n_clicks"), Input("submit-button", "n_clicks"),
     Input("close-verify-modal", "n_clicks")],
    [State("modal", "is_open"), State("verify-modal", "is_open")]
)
def toggle_modals(open_click, close_click, submit_click, close_verify_click, is_open, is_verify_open):
    ctx = dash.callback_context
    if not ctx.triggered:
        return False, False
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == "open-modal" and not is_open:
            return True, False
        elif button_id == "close-modal" and is_open:
            return False, False
        elif button_id == "submit-button" and is_open:
            return False, True  # Close the initial modal and open the verification modal
        elif button_id == "close-verify-modal" and is_verify_open:
            return False, False  # Close the verification modal
    return is_open, is_verify_open


@app.callback(
    [Output("error-alert", "is_open"),
     Output("verify-modal-body", "children")],
    [Input("submit-button", "n_clicks")],
    [State("name", "value"), State("email", "value"), State("message", "value")]
)
def submit_modal_form(n_clicks, name, email, message):
    if n_clicks > 0:
        if not all([name, email, message]):  # Check all fields are filled
            return True, ""
        if email.count("@") != 1:  # Check email is valid
            return True, ""
        if not email.endswith(".com") and not email.endswith(".org") and not email.endswith(".edu"):
            return True, ""
        else:
            add_user_contact(name, email, message)
            # [Your Email Sending Logic Here]
            # Close the alert and display email verification message
            return False, f"As a precaution, please verify your email in order to send this form. Check {email}"
    return False, ""


@app.callback(
    [Output("cookie-consent-offcanvas", "is_open"),
     Output("cookie-consent-offcanvas", "backdrop")],
    [Input("accept-button", "n_clicks"),
     Input("reject-button", "n_clicks")],
    [State("cookie-consent-offcanvas", "is_open"),
     State("cookie-consent-offcanvas", "backdrop")],
    prevent_initial_call=True
)
def toggle_offcanvas(accept, reject, is_open, backdrop):
    return is_open, backdrop


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
        margin=dict(t=2, r=20, l=20, b=2),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )

    return {'data': traces, 'layout': layout}


if __name__ == "__main__":

    app.run_server(debug=True)


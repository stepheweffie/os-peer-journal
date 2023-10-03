from dash import html
import dash_bootstrap_components as dbc

CONTACT = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Contact Us', className='mb-0'),
            html.Hr(),
    ])
    ]),
    dbc.Container([
        dbc.Form([
            dbc.Col([
                dbc.Label("Name", className="mr-2"),
                dbc.Input(type="text", id="input-name", placeholder="Enter your name"),
            ], className="mb-3"),

            dbc.Col([
                dbc.Label("Email", className="mr-2"),
                dbc.Input(type="email", id="input-email", placeholder="Enter your email"),
            ], className="mb-3"),

            dbc.Row([
                dbc.Col([
                dbc.Label("Message", className="mr-2"),
                dbc.Textarea(id="input-message", placeholder="Your message..."),
            ], className="mb-3"),
            ]),
            dbc.Button("Submit", id="submit-button", color="primary"),
        ]),
    ]),
    html.Div(id="contact-form-output")
    ])

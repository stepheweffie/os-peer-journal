from dash import html
import dash_bootstrap_components as dbc

login = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Login', className='mb-0'),
            html.Hr(),
    ])
    ]),
    dbc.Container([
        dbc.Form([
            dbc.Col([
                dbc.Label("Name", className="mr-2"),
                dbc.Input(type="text", id="login-input-name", placeholder="Enter your name"),
            ], className="mb-3"),

            dbc.Col([
                dbc.Label("Email", className="mr-2"),
                dbc.Input(type="email", id="login-input-email", placeholder="Enter your email"),
            ], className="mb-3"),

            dbc.Button("Submit", id="login-submit-button", color="primary"),
        ]),
    ]),
    html.Div(id="login-form-output")
    ])

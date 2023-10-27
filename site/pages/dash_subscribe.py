import dash_bootstrap_components as dbc
from dash import html


contact_form = html.Div([
    dbc.Button("Contact Sales", id="subscribe-collapse-button", className="mb-3", color="primary", n_clicks=0),
    dbc.Collapse(
        dbc.Form([
            dbc.Container([
                 dbc.Row([
                    dbc.Container([
                        dbc.Alert("Thank you for your submission. Please verify your email to send this form.",
                                  id='collapse-email-alert', color="dark", is_open=False),
                        dbc.Alert("All fields must be filled!", id='collapse-info-alert', color="primary",
                                  is_open=True),
                        dbc.Label("For More Information About Subscribing", className="mr-2"),
                        dbc.Col(dbc.Input(type="text", id="name-input", placeholder="First Name",
                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
                    dbc.Container([
                        dbc.Col(dbc.Input(type="text", id='last-name-input', placeholder="Last Name",
                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8"),
                dbc.Row([
                    dbc.Container([
                        dbc.Col(dbc.Input(type="text", id="institution-input", placeholder="Institution",
                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
                    dbc.Container([
                        dbc.Col(dbc.Input(type="text", id="phone-input", placeholder="Phone Number",
                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8"),
                dbc.Row([
                    dbc.Container([
                        dbc.Col(dbc.Input(type="email", id="contact-email-input", placeholder="Email",
                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8"),
                dbc.Row([
                    dbc.Col(dbc.Button("Submit", id="subscribe-contact-button", n_clicks=0, className="mt-3", color="primary"),
                            className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
                ], id="subscribe-contact-output", className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8",)
                ]),
        ]),
        id="subscribe-collapse", is_open=False
    )
], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-8")


SUBSCRIBE = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Subscribe', className='mb-12'),
            html.Hr(),
    ]),
    ]),
        dbc.Container([
                dbc.Col([
                    html.Div(style={
                      'backgroundImage': 'url("/static/wiredbrain27.svg")',
                      'backgroundSize': 'cover',
                      'backgroundPosition': 'center 55%',
                      'width': '100%',
                      'height': '40vh',
                      'display': 'flex',
                      'alignItems': 'left',
                      'justifyContent': 'left'})
                    ],
                    # f'{contact_text}',
                    className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
            ], style={'width': '100%'}),
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("We Have Plans")
                    , className="p-2 m-6 text-center", style={
                    'max-width': '100%',
                    'color': 'white'
                }),
        ])
    ]),
    dbc.Container([
        dbc.Row([
            dbc.Container([
                dbc.Col(html.Div([
                    dbc.Col(
                        html.H2("Education"), className="text-center"),
                    html.Hr(),
                    html.H5("Librarians"),
                    html.H6("Explain what it means here and how it works")],
                        className="col-xl-12 p-2 m-6"),
                        className="col-xl-12 m-1 p-2", style={
                    'max-width': '100%',
                    'color': 'white',
                    'border-radius': '50px 20px',
                    'border': '1px solid cyan'})
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-3", fluid=True),
            dbc.Container([
                dbc.Col(html.Div([
                    dbc.Col(
                        html.H2("Corporate"), className="text-center"),
                    html.Hr(),
                    html.H5("Businesses"),
                    html.H6("Explain what it means here and how it works")],
                                 className="col-xl-12 p-2 m-6"),
                        className="col-xl-12 m-1 p-2", style={
                    'max-width': '100%',
                    'color': 'white',
                    'border-radius': '50px 20px',
                    'border': '1px solid cyan'})
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-3", fluid=True),
            dbc.Container([
                dbc.Col(html.Div([
                    dbc.Col(
                        html.H2("NonProfit"), className="text-center"),
                    html.Hr(),
                    html.H5("Organizations"),
                    html.H6("Explain what it means here and how it works")],
                                 className="col-xl-12 p-2 m-6"),
                        className="col-xl-12 m-1 p-2", style={
                    'max-width': '100%',
                    'color': 'white',
                    'border-radius': '50px 20px',
                    'border': '1px solid cyan'})
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-3", fluid=True),
            dbc.Container([
                dbc.Col(html.Div([
                    dbc.Col(
                        html.H2("Government"), className="text-center"),
                    html.Hr(),
                    html.H5("Agencies"),
                    html.H6("Explain what it means here and how it works")],
                                 className="col-xl-12 p-2 m-6"),
                        className="col-xl-12 m-1 p-2", style={
                    'max-width': '100%',
                    'color': 'white',
                    'border-radius': '50px 20px',
                    'border': '1px solid cyan'})
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-3", fluid=True),
        ], className="m-2"),
        ], className="m-0", fluid=False),
    html.Hr(),
    contact_form
], fluid=False,
)


import dash_bootstrap_components as dbc
from dash import html


contact_form = html.Div([
    dbc.Button("Contact Sales", id="collapse-button", className="mb-3", color="primary"),
    dbc.Collapse(
        dbc.Form([
            dbc.Container([
                dbc.Label("For More Information About Subscribing", className="mr-2"),
                dbc.Row([
                    dbc.Col(dbc.Input(type="text", id="name-input", placeholder="First Name", className="mt-2")),
                    dbc.Col(dbc.Input(type="text", id='last-name-input', placeholder="Last Name", className="mt-2"))
                ]),
                dbc.Row([
                    dbc.Col(dbc.Input(type="text", id="institution-input", placeholder="Institution", className="mt-2")),
                    dbc.Col(dbc.Input(type="text", id="phone-input", placeholder="Phone Number", className="mt-2"))
                ]),
                dbc.Row([
                    dbc.Col(dbc.Input(type="email", id="contact-email-input", placeholder="Email", className="mt-2")),
                    dbc.Col(dbc.Button("Submit", id="contact-button", className="mt-3", color="primary"))
                ]),
            ]),
            html.Div(id="contact-output")
        ]),
        id="collapse"
    )
])
SUBSCRIBE = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Subscribe', className='mb-12'),
            html.Hr(),
    ]),
    ]),
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


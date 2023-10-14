from dash import html
import dash_bootstrap_components as dbc


contact = dbc.Container([
    html.Hr(),
    dbc.Row([
        dbc.Col(dbc.Button("Message", id="open-modal", className="mt-3", color="primary"),
                className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
    ], id="open-modal", className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8", ),
        dbc.Modal([
            dbc.ModalHeader("Contact Us"),
            dbc.ModalBody([
                dbc.Form([
                    dbc.Input(id="name", placeholder="Your name", type="text"),
                    dbc.Input(id="email", placeholder="Your email", type="email"),
                    dbc.Textarea(id="message", placeholder="Your message"),
                    html.P(id="output", style={"color": "white"})
            ]),
                dbc.ModalFooter([
                    dbc.Button("Close", id="close-modal", className="ml-auto", n_clicks=0, color="secondary"),
                    dbc.Button("Submit", id="submit-button", className="ml-2", n_clicks=0, color="secondary")
            ])
            ])
        ], id="modal"),

    dbc.Modal([
        dbc.Alert("Something wasn't filled out correctly!", id='error-alert', color="danger", is_open=False),
        # dbc.ModalHeader("Email Verification Required."),
        dbc.ModalBody(id='verify-modal-body'),
        dbc.ModalFooter(dbc.Button("Close", id="close-verify-modal", className="ml-auto"))
    ], id="verify-modal")
], fluid=True)

contact_text = 'For press inquires, business, or general questions, please contact us at:'

header = dbc.Container([
        dbc.Col([
            html.Div(style={
              'backgroundImage': 'url("/static/wiredbrain28.svg")',
              'backgroundSize': 'cover',
              'backgroundPosition': 'center 55%',
              'width': '100%',
              'height': '40vh',
              'display': 'flex',
              'alignItems': 'left',
              'justifyContent': 'left'})
            ],
            f'{contact_text}',
            className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
    ], style={'width': '100%'})


CONTACT = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Contact Us', className='mb-12'),
            html.Hr(),
    ]),
    ]),
    header,
    contact
])

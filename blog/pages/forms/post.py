import dash_bootstrap_components as dbc
import dash_html_components as html


post = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Prepare Post', className='mb-0'),
            html.Hr(),
    ])
    ]),
    dbc.Container([
        dbc.Form([
            dbc.Col([
                dbc.Label("Title", className="mr-2"),
                dbc.Input(type="text", id="login-input-name", placeholder="Enter your name"),
            ], className="mb-3"),
            dbc.Col([
                dbc.Label("Slug", className="mr-2"),
                dbc.Input(type="text", id="login-input-slug", placeholder="Enter your slug"),
            ], className="mb-3"),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Upload", className="mr-2"),
                    dbc.Input(type="file", id="login-input-upload", placeholder="Upload your file"),
                ], className="mb-3"),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Input(type="submit", id="login-input-submit", name='Submit', placeholder="Submit"),
                ], className="mb-3"),
        ]),
    ]),
]),
])


from dash import html
import dash_bootstrap_components as dbc

PEOPLE = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Who Are We?', className='mb-0'),
            html.Hr(),
    ])
    ]),
    dbc.Container([
                dbc.Col([
                    html.Div(style={
                      'backgroundImage': 'url("/static/wiredbrain29.svg")',
                      'backgroundSize': 'cover',
                      'backgroundPosition': 'center 75%',
                      'width': '100%',
                      'height': '40vh',
                      'display': 'flex',
                      'alignItems': 'left',
                      'justifyContent': 'left'})
                    ],
                    # f'{faq}',
                    className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
                html.Hr(),
            ], style={'width': '100%'}),
        ])

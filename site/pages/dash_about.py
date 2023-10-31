from dash import html
import dash_bootstrap_components as dbc
from .dash_body import map_body

with open('pages/text/about.html', 'r') as f:
    f = f.read()
    text1 = f[:491]
    text2 = f[491:1157]
    text3 = f[1157:1887]
    text4 = f[1887:3100]
    text5 = f[3100:3750]
text = html.Div([
            html.P(text1),
            html.P(text2),
            html.P(text3),
            html.P(text4),
            html.P(text5)
                 ])
about = 'This is some long string of text to describe the journal or blurb whichever is linked here'
ABOUT = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Center(html.H1('About', className='mb-12', style={'color': 'white', 'font-size': '100px'})),
            html.Hr(),
    ])
    ]),
    dbc.Container([
        dbc.Col([
            html.Div(style={
              'backgroundImage': 'url("/static/wiredbrain12.svg")',
              'backgroundSize': 'cover',
              'backgroundPosition': 'center 45%',
              'width': '100%',
              'height': '40vh',
              'display': 'flex',
              'alignItems': 'left',
              'justifyContent': 'left'})
            ],
            f'{about}',
            className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
        html.Hr(),
    ], style={'width': '100%'}),
    dbc.Row([
        dbc.Container([
            dbc.Col([
                text,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'width': '100%',
                                                                                   'color': 'whitesmoke',
                                                                                   'font-size': '1.2rem', }),
        ], style={'width': '100%'}),
    ]),
    map_body
])




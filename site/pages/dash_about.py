from dash import html
import dash_bootstrap_components as dbc
from .dash_map import map_body
from .dash_bodysection import about_header_video_section

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
                 ], style={'font-size': '1.6rem',
                           'color': 'whitesmoke'})

ABOUT = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Hr(),
    ])]),
    about_header_video_section,
    dbc.Row([
        dbc.Container([
            dbc.Col([
                map_body,
                text,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'width': '100%',
                                                                                   'color': 'whitesmoke',
                                                                                   'font-size': '1.2rem', }),
        ], style={'width': '100%'}),
    ])
])




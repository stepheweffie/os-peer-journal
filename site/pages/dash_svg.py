import dash_bootstrap_components as dbc
from dash import html


braincomp = dbc.Container([
    dbc.Row([
        dbc.Container([
            dbc.Col([
                html.Img(src='/static/braincomp.svg', height='600px', width='400px'),
            ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-6",
                style={'max-width': '100%'}),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
                style={'max-width': '100%'}),
        ])])

eyecomp = dbc.Container([
    dbc.Row([
        dbc.Container([
            dbc.Col([
                html.Img(src='/static/eyecomp.svg', height='600px', width='400px'),
            ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-6",
                style={'max-width': '100%'}),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
                style={'max-width': '100%'}),
        ])])

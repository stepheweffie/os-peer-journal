from dash import dcc, html
import dash_bootstrap_components as dbc
from .dash_toasts import toast1, toast2, placeholder
from .dash_bodyheader import body_header
from .dash_bodysection import video_section

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


neruovid = dbc.Container([
    html.Div(
        children=[
            html.Video(
                src='/static/neuropurp.mp4',
                controls=False,
                autoPlay=True,
                loop=True,
                style={
                    'width': '100%',
                    'maxWidth': '500px',  # set a max-width if needed
                    'height': 'auto'
            })])])


BODY = html.Div([
        body_header,
        dbc.Container([
            video_section,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
        dbc.Container([
            placeholder,
            toast2,
            placeholder,
            toast1,
            placeholder,
            braincomp,
            eyecomp,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'})])



sine_waves = dbc.Container([
        dcc.Graph(id='animated-graph')
    ],)





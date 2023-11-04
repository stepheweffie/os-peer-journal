from .dash_toasts import toast0, toast01, toast1
from dash import html
import dash_bootstrap_components as dbc


body_section = dbc.Container([
                dbc.Container([
                        dbc.Col([
                            toast0,
                            toast01,
                            toast1,
                    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8", style={'max-width': '100%'}),

])


video_section = html.Div(
    children=[
        html.Div(
            children=[
               body_section
            ],
            style={
                'position': 'relative',
                'zIndex': 2,
            }
        ),
        html.Video(
            src='/static/neuropurp.mp4',
            autoPlay=True,
            loop=True,
            muted=True,
            style={
                'position': 'absolute',
                'width': '100%',
                'left': 0,
                'top': 0,
                'height': '110%',
                'objectFit': 'cover',
                'zIndex': 1
            }
        )
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={
        'position': 'relative',
        'overflow': 'hidden',
    }
)

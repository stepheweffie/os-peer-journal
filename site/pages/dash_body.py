from dash import dcc, html
import dash_bootstrap_components as dbc
from .dash_toasts import toast1, toast2, placeholder
from .dash_bodyheader import body_header
from .dash_bodysection import video_section


BODY = html.Div([
        body_header,
        dbc.Container([
            video_section,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
        dbc.Container([
            placeholder,
            toast1,
            placeholder,
            toast2,
            placeholder,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'})])






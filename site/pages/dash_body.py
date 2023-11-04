from dash import html
import dash_bootstrap_components as dbc
from .dash_toasts import toast2, placeholder
from .dash_bodyheader import body_header
from .dash_bodysection import video_section, eye_body_section
from .dash_forms import email_toast

BODY = html.Div([
        body_header,
        dbc.Container([
            video_section,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
        dbc.Container([
            placeholder,
            placeholder,
            toast2,
            placeholder,
            eye_body_section,
            email_toast,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'})
])






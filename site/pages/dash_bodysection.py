from .dash_toasts import toast0, toast01, toast1, toast3
from .dash_svg import eyecomp, cogcomp
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

half_body_section = dbc.Container([
            html.Center(toast3),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
            style={'max-width': '100%'})

half_body_section2 = dbc.Container([
            html.Center(toast3),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
            style={'max-width': '100%'})


def _video_half_section(content, video_src):
    return html.Div(
        children=[
            html.Div(
                children=content,
                style={
                    'position': 'relative',
                    'zIndex': 2,
                }
            ),
            html.Video(
                src=video_src,
                autoPlay=True,
                loop=True,
                muted=True,
                style={
                    'position': 'absolute',
                    'width': '100%',
                    'left': 0,
                    'top': 0,
                    'height': '100%',
                    'objectFit': 'cover',
                    'zIndex': 1
                }
            )
        ],
        className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
        style={
            'position': 'relative',
            'overflow': 'hidden',
        }
    )


half_video_section = _video_half_section(half_body_section, '/static/blueneurons.mp4')
half_video_section2 = _video_half_section(half_body_section2, '/static/blueneurons.mp4')


eye_body_section = dbc.Container([
    dbc.Container([
            dbc.Col([
                eyecomp], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",)
       ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
    dbc.Container([
            dbc.Col([
              half_video_section], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")
        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%',
                                                                                 'margin-bottom': '25px'}),
    dbc.Container([
            dbc.Col([
                cogcomp], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",)
       ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
    dbc.Container([
        dbc.Col([
            half_video_section2], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%',
                                                                             'margin-bottom': '25px'}),
    html.Hr(),
], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'})


from .dash_toasts import toast0, toast01, toast1, toast3, toast4
from .dash_svg import eyecomp, cogcomp
from dash import html
import dash_bootstrap_components as dbc


VIDEO_body_section = dbc.Container([
                dbc.Container([
                        dbc.Col([
                            toast0,
                            toast01,
                            toast1,
                    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8", style={'max-width': '100%'}),

])


def half_section(content):
    return dbc.Container([
        content,
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
        style={'max-width': '100%'})


def _video_section(content, video_src):
    return html.Div(
        children=[
            html.Div(
                children=[
                    content
                ],
                style={
                    'position': 'relative',
                    'zIndex': 2,
                }),
            html.Video(
                src= video_src,
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
                })
        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={
            'position': 'relative',
            'overflow': 'hidden',
        })


def video_heading(heading):
    return dbc.Container([
        html.Center(html.H1(f'{heading}', className='mb-12', style={'color': 'whitesmoke',
                                                                    'font-family': 'Triad',
                                                                    'font-size': '5rem',
                                                                    'background': 'rgba(0, 0, 0, .9)',
                                                                    'margin-top': '5%'})),
    ])


about_text = 'About'
sub_text = 'Subscribe'
video_body_section = _video_section(VIDEO_body_section, '/static/neuropurp.mp4')
half_body_section = half_section(toast3)
half_body_section2 = half_section(toast4)
half_video_section = _video_section(half_body_section, '/static/blueneurons.mp4')
half_video_section2 = _video_section(half_body_section2, '/static/blueneurons.mp4')
about_header_video_section = _video_section(video_heading(about_text), '/static/neurospiral.mp4')
sub_header_video_section = _video_section(video_heading(sub_text), '/static/neurospike.mp4')

eye_body_section = dbc.Container([
    dbc.Container([
            dbc.Col([
                eyecomp], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",)
       ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
    dbc.Container([
            dbc.Col([
                html.Center(half_video_section),
              ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")
        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%',
                                                                                 'margin-bottom': '25px'}),
    dbc.Container([
            dbc.Col([
                cogcomp], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",)
       ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
    dbc.Container([
        dbc.Col([
            html.Center(half_video_section2),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%',
                                                                             'margin-bottom': '25px'}),
], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'})


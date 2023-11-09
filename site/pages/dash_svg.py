import dash_bootstrap_components as dbc
from dash import html


braincomp = dbc.Container([
    dbc.Row([
        dbc.Container([
            dbc.Col([
                html.Img(src='/static/braincomp.svg'),
            ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-6",
                style={'max-width': '100%'}),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
                style={'max-width': '100%'}),
        ])])

eyecomp = html.Div(html.Img(src='/static/eyecomp.svg', style={'position': 'absolute',
                                                              'top': '0',
                                                              'width': '110%',
                                                              'height': '110%',
                                                              }),
                   className="d-flex align-items-center justify-content-center",
                   style={'position': 'relative',
                   'padding-top': '50%'})

cogcomp = html.Div(html.Img(src='/static/cogcomp.svg', style={'position': 'absolute',
                                                              'top': '0',
                                                              'width': '110%',
                                                              'height': '110%',
                                                              }),
                   className="d-flex align-items-center justify-content-center",
                   style={'position': 'relative',
                   'padding-top': '50%'})

philcomp = html.Div(html.Img(src='/static/philcomp.svg', style={'position': 'absolute',
                                                              'top': '0',
                                                              'width': '110%',
                                                              'height': '110%',
                                                              }),
                   className="d-flex align-items-center justify-content-center",
                   style={'position': 'relative',
                   'padding-top': '50%'})
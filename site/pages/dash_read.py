from dash import html
import dash_bootstrap_components as dbc
from .dash_cards import first_card, second_card
from .dash_toasts import toast2
blog = []
articles = []

READ = dbc.Container([
            dbc.Container([
                html.Video(
                    src='/static/neuropurpspin.mp4',
                    autoPlay=True,
                    loop=True,
                    muted=True,
                    style={
                        'position': 'relative',
                        'width': '100%',
                        'left': 0,
                        'top': 20,
                        'height': 'auto',
                        'objectFit': 'cover',
                        'zIndex': 1
                }),]),
            html.Div([
                dbc.Row([
                    dbc.Container([
                        html.Br(),
                        dbc.Col([
                            html.Center(html.H1('Scideology', className='mb-12', style={'color': 'white',
                                                                                        'font-size': '50px',
                                                                                        'font-family': 'Aotani'})),
                            html.Center(html.Img(src='/static/book.svg', height='30px', width='50px')),
                            html.Hr(),
                            first_card,
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-6", style={'max-width': '100%'}),
                    dbc.Container([
                        html.Br(),
                        dbc.Col([
                            html.Center(html.H1('Peer-Review', className='mb-12', style={'color': 'white',
                                                                                         'font-size': '50px',
                                                                                         'font-family': 'Aotani'})),
                            html.Center(html.Img(src='/static/mtone.svg', height='30px', width='50px')),
                            html.Hr(),
                            second_card
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-6", style={'max-width': '100%'})])
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%',
                                                                                     'position': 'relative'}),
            dbc.Container([
                html.Br(),
                toast2,
                html.Hr(),
                html.Img(src='/static/humanwork.svg', height='100%', width='120%', style={'position': 'relative',
                                                                                         'left': '-10.00%'}),
                html.Hr(),
                toast2,
                html.Hr(),
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'})])



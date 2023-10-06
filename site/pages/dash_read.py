from dash import html
import dash_bootstrap_components as dbc


blog = []
articles = []
text_1 = 'This is some long string of text to describe the journal or blurb whichever is linked here' \
         ' it needs to be long enough to fill the card and look good' \
         ' This is some long string of text to describe the journal or blurb whichever is linked here'
text_2 = text_1

first_card = dbc.Container([
        dbc.Card(
            [
                dbc.CardImg(
                    src="/static/slide4.svg",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody(
                        [
                            html.H4("Read The Blurb", className="card-title"),
                            html.P(
                                f'{text_1}',
                                className="card-text col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6",
                                style={'width': '100%'},
                            ),
                            html.Div(
                        [
                            dbc.Button("Go To It", color="secondary"),
                        ],
                                className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'},
                            ),
                        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}
                    ),

                ),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}
        ),
        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'})


second_card = dbc.Container([
        dbc.Card(
            [
                dbc.CardImg(
                    src="/static/slide5.svg",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody(
                        [
                            html.H4("Read The Journal", className="card-title"),
                            html.P(
                                f'{text_2}',
                                className="card-text col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6",
                                style={'width': '100%'},
                            ),
                            html.Div(
                        [
                            dbc.Button("Go To It", color="secondary"),
                        ],
                                className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'},
                            ),
                        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}
                    ),

                ),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}
        ),
        ], className="mb-3", style={'width': '100%'})

READ = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Read', className='mb-0'),
            html.Hr(),
    ])
    ]),

    dbc.Row([
        dbc.Container([
        dbc.Col([
            html.H2('Sciencey Stuff Blog', className='m-3 text-left'),
            first_card,
            ]),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'max-width': '100%'}),
        dbc.Container([
        dbc.Col([
            html.H2('Peer-Reviewed Articles', className='m-3 text-left'),
            second_card,
            ]),
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'max-width': '100%'}),
    ]),
    ], fluid=False)


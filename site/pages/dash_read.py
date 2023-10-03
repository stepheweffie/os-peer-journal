from dash import html, dcc
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
                                className="card-text",
                            ),
                            html.Div(
                        [
                            dbc.Button("Go To It", color="dark"),
                        ],
                                className="d-grid gap-2",
                            ),
                        ],
                    ),

                ),
            ],
            style={"width": "28rem"},
        ),
        ])


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
                                className="card-text",
                            ),

                            html.Div(
                        [
                            dbc.Button("Go To It", color="dark"),
                        ],
                                className="d-grid gap-2",
                            ),
                        ],
                    ),

                ),
            ],
            style={"width": "28rem"},
        ),
        ])


READ = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Read', className='mb-0'),
            html.Hr(),
    ])
    ]),
    dbc.Container([
        dbc.Col(html.Div([
            dbc.Col(
                html.H2("Blog"), className="m-3 text-left"),
            dbc.Col(first_card, className='m-1 col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-3'),
            ]),
            className='m-3 col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-3'),
        html.Hr(),
        dbc.Col(html.Div([
            dbc.Col(
                html.H2("Peer-Review"), className="m-3 text-left"),
            dbc.Col(second_card, className='m-1 col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-3'),
            ]),
            className='m-3 col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-3'),
        html.Hr(),
        ])
    ])

# Define callback to update graph

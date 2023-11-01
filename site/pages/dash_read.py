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
                    src="/static/wiredbrain4.svg",
                    top=True,
                    style={"opacity": 0.3},
                ),
                dbc.CardImgOverlay(
                    dbc.CardBody(
                        [
                            html.H4("Read The Blog", className="card-title"),
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
    html.Article(
        dbc.Card(
            [
                dbc.CardImg(
                    src="/static/wiredbrain9.svg",
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
                                style={'width': '100%'}),
                            html.Div(
                        [
                            dbc.Button("Go To It", color="secondary"),
                        ],
                                className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'},),
                        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
                ),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
    )], className="mb-3", style={'width': '100%'})

READ = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Center(html.H1('Read', className='mb-12', style={'color': 'white', 'font-size': '100px'})),
            html.Hr(),
    ])]),

    dbc.Container([
        dbc.Col([
            html.Div(style={
              'backgroundImage': 'url("/static/wiredbrain32.svg")',
              'backgroundSize': 'cover',
              'backgroundPosition': 'center 45%',
              'width': '100%',
              'height': '40vh',
              'display': 'flex',
              'alignItems': 'left',
              'justifyContent': 'left'}),
            ],
            # f'{read}',
            className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
        ], style={'width': '100%'}),

    dbc.Row([
        dbc.Container([
            html.Br(),
            dbc.Col([
                html.Center(html.H1('Scideology', className='mb-12', style={'color': 'white', 'font-size': '50px'})),
                html.Center(html.Img(src='/static/book.svg', height='30px', width='50px')),
                first_card,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'max-width': '100%'}),
        dbc.Container([
            html.Br(),
            dbc.Col([
                html.Center(html.H1('Peer-Review', className='mb-12', style={'color': 'white', 'font-size': '50px'})),
                html.Center(html.Img(src='/static/mtone.svg', height='30px', width='50px')),
                second_card]),
        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'max-width': '100%'})]),
    ], fluid=False)


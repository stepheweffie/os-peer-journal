import dash_bootstrap_components as dbc
from dash import html

text_1 = 'This is some long string of text to describe the journal or blurb whichever is linked here' \
         ' it needs to be long enough to fill the card and look good' \
         ' This is some long string of text to describe'
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
                                className="card-text col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
                                style={'width': '100%'}),
                            html.Div([
                                dbc.Button("Go To It", color="secondary", href='/blog', target='blank',
                                           style={'width': '50%',
                                                  'margin-left': '20px'})
                            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
                                style={'width': '100%',
                                       'margin': '-10px',
                                       'position': 'relative'})
                            ,
                        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'width': '100%'}
                    )),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'width': '100%'})


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
                                className="card-text col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
                                style={'width': '100%',
                                       'height': '100%'}),
                            html.Div([
                                dbc.Button("Go To It", color="secondary", href='/journal', target='_blank',
                                           style={'width': '50%',
                                                  'margin-left': '20px'})
                        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
                                style={'width': '100%',
                                       'height': '100%',
                                       'margin': '-10px',
                                       'position': 'relative'}),

                        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'width': '100%',
                                                                                                 }),
                ),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%',
                                                                                   'height': '100%',
                                                                                   }),
    )], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'width': '100%'})

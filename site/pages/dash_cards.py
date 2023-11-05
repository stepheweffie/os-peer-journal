import dash_bootstrap_components as dbc
from dash import html

text_1 = 'This is some long string of text to describe the journal or blurb whichever is linked here it needs to be ' \
         'long enough to fill the card and '

text_2 = text_1[:-100]


first_card = dbc.Container([
    html.Article(
        dbc.Card([dbc.CardImg(
                    src="/static/wiredbrain4.svg",
                    top=True,
                    style={"opacity": 0.1}),
                    dbc.CardImgOverlay(
                    dbc.CardBody([html.H4("Read The blog", className="card-title"),
                                 html.P(
                                f'{text_1}',
                                className="card-text"),
                            html.Div(dbc.Button("Go To It", color="secondary", href='/blog', target='blank',
                                     className="position-absolute bottom-0 start-0",
                                     style={'width': 'auto', 'margin': '0 20px 20px 20px'}),
                                     className="w-100 h-100",
                                     style={'position': 'relative'})],
                                 className="d-flex flex-column h-100"),
                )], className="h-100 gradient-border"))], className="h-100")



second_card = dbc.Container([
    html.Article(
        dbc.Card([dbc.CardImg(
                    src="/static/wiredbrain9.svg",
                    top=True,
                    style={"opacity": 0.1}),
                    dbc.CardImgOverlay(
                    dbc.CardBody([html.H4("Read The Journal", className="card-title"),
                                 html.P(
                                f'{text_2}',
                                className="card-text"),
                            html.Div(dbc.Button("Go To It", color="secondary", href='/blog', target='blank',
                                     className="position-absolute bottom-0 start-0",
                                     style={'width': 'auto', 'margin': '0 20px 20px 20px'}),
                                     className="w-100 h-100",
                                     style={'position': 'relative'})],
                                 className="d-flex flex-column h-100"),
                )], className="h-100 gradient-border"))], className="h-100")

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

education_card =  dbc.Container([
                dbc.Col(
                    html.Div([
                        dbc.Card([
                            dbc.CardBody([
                                dbc.Col(
                                    html.H2("Education"), className="text-center"),
                                html.Hr(),
                                html.H5("Librarians"),
                                html.H6("Faculty must be covered by an institutional plan."),
                                html.Center(html.Img(src='/static/puzz.svg', height='50px', width='75px')),
                            ])])],
                        className="col-xl-12 p-2 m-6"),
                    className="col-xl-12 m-1 p-2", style={
                        'max-width': '100%',
                        'color': 'white',
                        'border-radius': '50px 20px',
                        'border': '1px solid cyan'}),
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-5", fluid=True)

corporate_card = dbc.Container([
                dbc.Col(
                    html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Col(
                                html.H2("Corporate"), className="text-center"),
                            html.Hr(),
                            html.H5("Businesses"),
                            html.H6("Maintain an edge in the marketplace."),
                            html.Center(html.Img(src='/static/brief.svg', height='50px', width='75px')),
                                             ])])],
                        className="col-xl-12 p-2 m-6"),
                    className="col-xl-12 m-1 p-2", style={
                                                        'max-width': '100%',
                                                        'color': 'white',
                                                        'border-radius': '50px 20px',
                                                        'border': '1px solid cyan'})
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-5", fluid=True)

non_profit_card = dbc.Container([
                dbc.Col(html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Col(
                                html.H2("NonProfit"), className="text-center"),
                            html.Hr(),
                            html.H5("Organizations"),
                            html.H6("NonGovernment labs working for better tech."),
                            html.Center(html.Img(src='/static/heart.svg', height='50px', width='75px')),
                        ])])],
                                 className="col-xl-12 p-2 m-6"),
                        className="col-xl-12 m-1 p-2", style={
                    'max-width': '100%',
                    'color': 'white',
                    'border-radius': '50px 20px',
                    'border': '1px solid cyan'})
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-5", fluid=True)



subscribe_cards = dbc.Row([
           education_card,
           corporate_card,
           non_profit_card,

        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")


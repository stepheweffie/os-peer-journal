import dash_bootstrap_components as dbc
from dash import html
from .dash_forms import email_toast, contact_form
from .dash_bodysection import sub_header_video_section
from .dash_cards import subscribe_cards
SUBSCRIBE = dbc.Container([
    sub_header_video_section,
        dbc.Container([
            dbc.Row([
                dbc.Container([
                    dbc.Col(html.H2("Individuals Can Read And Cite Freely")
                            , className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 p-2 m-6 text-center",
                            style={'max-width': '100%', 'color': 'white', 'font-family': 'Aotani'}),
                    html.Br()]),
                dbc.Col([
                   html.Br(),
                   html.H2("Institutional Plans", className="text-center", style={
                        'max-width': '100%',
                        'color': 'white',
                        'font-size': '50px',
                        'font-family': 'Aotani'}),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'marginRight': '0px'}),
                html.Br(),
        ]), subscribe_cards,
    ]),

            html.Br(),
            html.Hr(),
            html.Br(),
            dbc.Container([
            dbc.Col(html.Div([
                dbc.Col([
                    html.Center(html.H2("For More Information", className="text-center",
                                        style={'color': 'white',
                                               'font-size': '50px',
                                               'font-family': 'Aotani'})),
                    html.Center(html.Img(src='/static/chat.svg', height='50px', width='75px')),
                    html.Br(),
                    html.Center(contact_form)])],
                    className="col-xl-12 m-1 p-2", style={
                    'max-width': '100%',
                    'color': 'white',
                    'border-radius': '50px 20px',
                    'border': '1px solid cyan'}))
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 p-10", fluid=True),
        html.Br(),
    email_toast
    ], fluid=True)




import dash_bootstrap_components as dbc
from dash import html

logo = html.Img(src='/static/bclogoerbostrans.svg', height='150px', width='350px',
                style={'margin': '0px', 'padding': '0px', 'display': 'block', 'float': 'left',
                       'position': 'absolute', 'top': '-50px', 'left': '0px', 'z-index': '1000'})
navbar = dbc.NavbarSimple(
    children=[
        html.Br(),
        dbc.NavItem(dbc.NavLink("Read", href="/read", style={'color': 'white',
                                                             'font-size': '18px',
                                                             'font-family': 'Aotani',
                                                             })),
        dbc.NavItem(dbc.NavLink("Subscribe", href="/subscribe", style={'color': 'white', 'font-size': '18px',
                                                                       'font-family': 'Aotani'})),
        dbc.NavItem(dbc.NavLink("About", href="/about", style={'color': 'white', 'font-size': '18px',
                                                               'font-family': 'Aotani'})),
    ],
    brand=logo,
    brand_href="http://127.0.0.1:8050/",
    color="dark",
    dark=True,
    style={'background-color': '#000000', 'font-size': '18px',
           'font-family': 'Aotani',
           'top': '2px',
           'bottom': '10px',
           'left': '0px',
           'right': '0px'}
)

NAVBAR = dbc.Container([navbar], fluid=True, style={'display': 'block',
                                                    'float': 'left',
                                                    'position': 'relative',
                                                    'top': '0px',
                                                    'left': '0px',
                                                    'right': '0px',
                                                    'margin-bottom': '10px'})


import dash_bootstrap_components as dbc
from dash import html

main_navbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink("", href="/", style={'color': 'white', 'font-size': '20px'}),
        dbc.NavItem(dbc.NavLink("Read", href="/read", style={'color': 'white', 'font-size': '20px'})),
        dbc.NavItem(dbc.NavLink("Subscribe", href="/subscribe", style={'color': 'white', 'font-size': '20px'})),
        dbc.NavItem(dbc.NavLink("About", href="/about", style={'color': 'white', 'font-size': '20px'})),
    ],
    brand="Login/Register",
    brand_href="http://127.0.0.1:5000/subscriber/login",
    color="dark",
    dark=True,
)
logo = html.Img(src='/static/bclogoillusory.svg', height='150px', width='350px',
                style={'margin': '0px', 'padding': '0px', 'display': 'block', 'float': 'left',
                       'position': 'absolute', 'top': '-50px', 'left': '0px', 'z-index': '1000'})
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Read", href="/read", style={'color': 'white', 'font-size': '18px'})),
        dbc.NavItem(dbc.NavLink("Subscribe", href="/subscribe", style={'color': 'white', 'font-size': '18px'})),
        dbc.NavItem(dbc.NavLink("About", href="/about", style={'color': 'white', 'font-size': '18px'})),
    ],
    brand=logo,
    brand_href="http://127.0.0.1:8050/",
    color="dark",
    dark=True,
)

MAINNAV = main_navbar
NAVBAR = navbar


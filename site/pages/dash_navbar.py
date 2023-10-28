import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink("", href="/", style={'color': 'white', 'font-size': '20px'}),
        dbc.NavItem(dbc.NavLink("Read", href="/read", style={'color': 'white', 'font-size': '20px'})),
        dbc.NavItem(dbc.NavLink("Subscribe", href="/subscribe", style={'color': 'white', 'font-size': '20px'})),
        dbc.NavItem(dbc.NavLink("About", href="/about", style={'color': 'white', 'font-size': '20px'})),
    ],
    brand="Login/Register",
    brand_href="http://127.0.0.1:5000/subscriber/login",
    color="black",
    dark=True,
)

NAVBAR = navbar

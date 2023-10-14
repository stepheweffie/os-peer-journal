import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Read", href="/read", style={'color': 'white', 'font-size': '20px'})),
        dbc.NavItem(dbc.NavLink("Subscribe", href="/subscribe", style={'color': 'white', 'font-size': '20px'})),
        dbc.NavItem(dbc.NavLink("About", href="/about", style={'color': 'white', 'font-size': '20px'})),
        dbc.NavItem(dbc.NavLink("People", href="/people", style={'color': 'white', 'font-size': '20px'})),
        dbc.NavItem(dbc.NavLink("FAQ", href="/faq", style={'color': 'white', 'font-size': '20px'})),
        dbc.NavItem(dbc.NavLink("Contact", href="/contact", style={'color': 'white', 'font-size': '20px'})),
    ],
    brand="Login/Register",
    brand_href="/register",
    color="black",
    dark=True,
)

NAVBAR = navbar

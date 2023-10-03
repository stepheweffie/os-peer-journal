import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Read", href="/read")),
        dbc.NavItem(dbc.NavLink("Subscribe", href="/subscribe")),
        dbc.NavItem(dbc.NavLink("About", href="/about")),
        dbc.NavItem(dbc.NavLink("People", href="/people")),
        dbc.NavItem(dbc.NavLink("FAQ", href="/faq")),
        dbc.NavItem(dbc.NavLink("Contact", href="/contact")),
    ],
    brand="Login/Register",
    brand_href="/register",
    color="dark",
    dark=True,
)

NAVBAR = navbar

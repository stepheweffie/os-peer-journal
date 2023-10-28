from dash import html
import dash_bootstrap_components as dbc

FOOTER = dbc.Container([
    dbc.Row([
        html.Hr(),
        dbc.Col([
            dbc.NavItem(dbc.NavLink("Contact", href="/contact", style={'color': 'white', 'font-size': '20px'})),
            dbc.NavItem(dbc.NavLink("FAQ", href="/faq", style={'color': 'white', 'font-size': '20px'})),
            dbc.NavItem(dbc.NavLink("People", href="/people", style={'color': 'white', 'font-size': '20px'})),
            html.Br(),
        ]),
        dbc.Col([
            dbc.NavItem(dbc.NavLink("Terms of Use", href="/terms", style={'color': 'white', 'font-size': '20px'})),
            dbc.NavItem(dbc.NavLink("Privacy Policy", href="/privacy", style={'color': 'white', 'font-size': '20px'})),
            dbc.NavItem(dbc.NavLink("Accessibility", href="/accessibility", style={'color': 'white',
                                                                                   'font-size': '20px'})),
            html.Br(),
        ]),
        html.Hr(className='m-40'),
])], className='m-40', style={'width': '100%'})


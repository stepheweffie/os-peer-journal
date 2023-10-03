from dash import dcc, html
import dash_bootstrap_components as dbc

ABOUT = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('About Us', className='mb-0'),
            html.Hr(),
    ])
    ])
    ])

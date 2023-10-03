from dash import dcc, html
import dash_bootstrap_components as dbc

PRIVACY = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Privacy', className='mb-0'),
            html.Hr(),
    ])
    ])
    ])


from dash import html
import dash_bootstrap_components as dbc

TERMS = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Terms of Service', className='mb-0'),
            html.Hr(),
    ])
    ])
    ])

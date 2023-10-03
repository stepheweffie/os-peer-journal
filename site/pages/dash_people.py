from dash import dcc, html
import dash_bootstrap_components as dbc

PEOPLE = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Who Are We?', className='mb-0'),
            html.Hr(),
    ])
    ])
    ])

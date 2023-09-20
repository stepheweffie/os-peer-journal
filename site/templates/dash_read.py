from dash import html
import dash_bootstrap_components as dbc

read = html.Div([
    dbc.Container([
        html.H1('An Article Title'),
        html.P('Article blurb goes here.'),
])
])


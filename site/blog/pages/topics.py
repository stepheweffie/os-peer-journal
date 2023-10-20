import dash
from dash import html

dash.register_page(__name__, name='Topics', path='/read/topics')

layout = html.Div([
    html.H1('This is our Topics page'),
    html.Div('This is our Topics page content.'),
    ])



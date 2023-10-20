import dash
from dash import html

dash.register_page(__name__, name='Guide', path='/read/guide')

layout = html.Div([
    html.H1('This is our Blog page'),
    html.Div('This is our Blog page content.'),
])


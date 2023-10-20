import dash
from dash import html

dash.register_page(__name__, name="Posts", path="/read/posts")

layout = html.Div([
    html.H1('This is our Posts page'),
    ])
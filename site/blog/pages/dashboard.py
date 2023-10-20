import dash
from dash import html
from .forms.post import post

dash.register_page(__name__, name="Dashboard", path="/dashboard")

layout = html.Div([
    html.H1('This is our Dashboard page'),
    post
])
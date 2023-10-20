from dash import html
import dash
from .forms.login import login

dash.register_page(__name__, name='Login', path='/login')

layout = html.Div([
    html.H1('This is our Login page'),
    login,
])


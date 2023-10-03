from dash import html, dcc
from dash.dependencies import Input, Output
from pages.dash_navbar import NAVBAR
from pages.dash_body import BODY
import dash
app = dash.Dash(__name__)

READ = html.Div([
    html.H1('Read'),
    html.P('Articles are listed here.')
])

app.layout = html.Div([html.H1('Dash URL routing'), dcc.Location(id='url'), NAVBAR, html.Div(id='display-url-info'),])

paths = dict()
paths['/'] = BODY
paths['/read'] = READ
paths['/subscribe'] = 'subscribe_layout'
paths['/about'] = 'about_layout'
paths['/people'] = 'people_layout'


@app.callback(
    Output('display-url-info', 'children'),
    [Input('url', 'href'),
     Input('url', 'pathname')]
)
def display_url(href, pathname):
    if pathname in paths:
        return paths[pathname]
    return [
        html.P(f"Full URL (href): {href}"),
        html.P(f"Pathname: {pathname}")
    ]


if __name__ == '__main__':
    app.run_server(debug=True)

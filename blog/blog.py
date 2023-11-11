import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
from flask import Flask

server = Flask(__name__)

app = Dash(external_stylesheets=[dbc.themes.QUARTZ],
           server=server,
           meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
           url_base_pathname='/blog/')
app.title = 'Scideology'
server.secret_key = 'secret_key'
server.config['SESSION_TYPE'] = 'filesystem'


def navbar():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    html.Div(page["name"], className="ms-2"),
                    href='/blog' + page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/read")
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    )


app.layout = html.Div([
    navbar(),
    html.H1('Blog App'),
    dash.page_container,
])

if __name__ == '__main__':
    app.run(debug=True)
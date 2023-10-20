# This is a Dash app subapp in the main Dash app
import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, url_base_pathname='/blog/')
server = app.server


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
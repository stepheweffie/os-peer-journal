from dash import html
import dash_bootstrap_components as dbc

body_header = dbc.Row([
    dbc.Container([
        dbc.Col([
            html.H1("An Academic Journal That Makes Sense.", className="mb-0",
                    style={'color': 'white',
                           'font-size': '75px',
                           'font-family': 'Akron'}),
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 mt-30", style={'max-width': '100%'}),
    dbc.Container([

], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 mb-10", style={'max-width': '100%'}),
], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'})
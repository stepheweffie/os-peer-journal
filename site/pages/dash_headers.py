import dash_bootstrap_components as dbc
from dash import html


title = ''
image = ''
text = ''

header = dbc.Row([
                dbc.Col([
                    html.Center(html.H1(f'{title}', className='mb-12', style={'color': 'white', 'font-size': '100px'})),
                    html.Hr()])]),
dbc.Container([
    dbc.Col([
        html.Div(style={
                  'backgroundImage': f'{image}',
                  'backgroundSize': 'cover',
                  'backgroundPosition': 'center 45%',
                  'width': '100%',
                  'height': '40vh',
                  'display': 'flex',
                  'alignItems': 'left',
                  'justifyContent': 'left'}),
                ],
            f'{text}',
            className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
            ], style={'width': '100%'})



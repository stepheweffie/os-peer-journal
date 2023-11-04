import dash_bootstrap_components as dbc
from dash import html
from .dash_forms import contact_form, email_toast

SUBSCRIBE = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Center(html.H1('Scribe', className='mb-12',
                                style={'color': '#00F0FF',
                                       'font-size': '5rem',
                                       'font-family': 'Triad'})),
            html.Hr(),
    ]),
    ]),
    dbc.Container([
        dbc.Col([
            html.Div(style={
              'backgroundImage': 'url("/static/wiredbrain27.svg")',
              'backgroundSize': 'cover',
              'backgroundPosition': 'center 55%',
              'transition': 'background-size 0.5s ease',
              'hover': 'background-size 1s ease',
              'backgroundRepeat': 'no-repeat',
              'width': '100%',
              'height': '40vh',
              'display': 'flex',
              'alignItems': 'left',
              'justifyContent': 'left'}, className='zoom-out-div')
            ],
            # f'{contact_text}',
            className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
    ], style={'width': '100%'}),
    dbc.Container([
        dbc.Row([
            dbc.Container([
                dbc.Col(html.H2("Individuals Can Read And Cite Freely")
                        , className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 p-2 m-6 text-center",
                        style={'max-width': '100%', 'color': 'white', 'font-family': 'Aotani'}),
                html.Br()]),
            dbc.Col([
               html.Br(),
               html.H2("Institutional Plans", className="text-center", style={
                    'max-width': '100%',
                    'color': 'white',
                    'font-size': '50px',
                    'font-family': 'Aotani'}),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'marginRight': '0px'}),
            html.Br(),
        ])
    ]),
    dbc.Container([
        dbc.Row([

            dbc.Container([
                dbc.Col(
                    html.Div([
                        dbc.Card([
                            dbc.CardBody([
                                dbc.Col(
                                    html.H2("Education"), className="text-center"),
                                html.Hr(),
                                html.H5("Librarians"),
                                html.H6("Faculty must be covered by an institutional plan."),
                                html.Center(html.Img(src='/static/puzz.svg', height='50px', width='75px')),
                            ])])],
                        className="col-xl-12 p-2 m-6"),
                    className="col-xl-12 m-1 p-2", style={
                        'max-width': '100%',
                        'color': 'white',
                        'border-radius': '50px 20px',
                        'border': '1px solid cyan'}),
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-5", fluid=True),

            dbc.Container([
                dbc.Col(
                    html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Col(
                                html.H2("Corporate"), className="text-center"),
                            html.Hr(),
                            html.H5("Businesses"),
                            html.H6("Maintain an edge in the marketplace."),
                            html.Center(html.Img(src='/static/brief.svg', height='50px', width='75px')),
                                             ])])],
                        className="col-xl-12 p-2 m-6"),
                    className="col-xl-12 m-1 p-2", style={
                                                        'max-width': '100%',
                                                        'color': 'white',
                                                        'border-radius': '50px 20px',
                                                        'border': '1px solid cyan'})
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-5", fluid=True),

            dbc.Container([
                dbc.Col(html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Col(
                                html.H2("NonProfit"), className="text-center"),
                            html.Hr(),
                            html.H5("Organizations"),
                            html.H6("NonGovernment labs working for better tech."),
                            html.Center(html.Img(src='/static/heart.svg', height='50px', width='75px')),
                        ])])],
                                 className="col-xl-12 p-2 m-6"),
                        className="col-xl-12 m-1 p-2", style={
                    'max-width': '100%',
                    'color': 'white',
                    'border-radius': '50px 20px',
                    'border': '1px solid cyan'})
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-5", fluid=True),

            dbc.Container([
                dbc.Col(html.Div([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Col(
                                html.H2("Government"), className="text-center"),
                            html.Hr(),
                            html.H5("Agencies"),
                            html.H6("Beyond health research and discovery."),
                            html.Center(html.Img(src='/static/gov.svg', height='50px', width='75px')),
                   ])])],
                                 className="col-xl-12 p-2 m-6"),
                        className="col-xl-12 m-1 p-2", style={
                    'max-width': '100%',
                    'color': 'white',
                    'border-radius': '50px 20px',
                    'border': '1px solid cyan'})
                ], className="col-xs-12 col-sm-12 col-md-6 col-lg-6 col-xl-5", fluid=True),


        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
        ], className="m-0", fluid=True),
    html.Br(),
    html.Hr(),
    html.Br(),
    dbc.Container([
            dbc.Col(html.Div([
                dbc.Col([
                    html.Center(html.H2("For More Information", className="text-center",
                                        style={'color': 'white',
                                               'font-size': '50px',
                                               'font-family': 'Aotani'})),
                    html.Center(html.Img(src='/static/chat.svg', height='50px', width='75px')),
                    html.Br(),
                    html.Center(contact_form)])],
                    className="col-xl-12 m-1 p-2", style={
                    'max-width': '100%',
                    'color': 'white',
                    'border-radius': '50px 20px',
                    'border': '1px solid cyan'}))
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 p-10", fluid=True),
    html.Br(),
    email_toast
    ], fluid=True)




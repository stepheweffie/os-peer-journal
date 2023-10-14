from dash import html
import dash_bootstrap_components as dbc

FAQ = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('FAQ', className='mb-0'),
            html.Hr(),
    ])
    ]),
    dbc.Container([
                dbc.Col([
                    html.Div(style={
                      'backgroundImage': 'url("/static/wiredbrain30.svg")',
                      'backgroundSize': 'cover',
                      'backgroundPosition': 'center 25%',
                      'width': '100%',
                      'height': '40vh',
                      'display': 'flex',
                      'alignItems': 'left',
                      'justifyContent': 'left'})
                    ],
                    # f'{faq}',
                    className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
                html.Hr(),
            ], style={'width': '100%'}),
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P("This is the content of the first section"),
                    dbc.Button("Click here"),
                ],
                title="Item 1",
            ),
            dbc.AccordionItem(
                [
                    html.P("This is the content of the second section"),
                    dbc.Button("Don't click me!", color="danger"),
                ],
                title="Item 2",
            ),
            dbc.AccordionItem(
                "This is the content of the third section",
                title="Item 3",
            ),
        ],
    )
    ])

from dash import html
import dash_bootstrap_components as dbc

FAQ = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('FAQ', className='mb-0'),
            html.Hr(),
    ])
    ]),
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

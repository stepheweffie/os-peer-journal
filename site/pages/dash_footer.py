from dash import html
import dash_bootstrap_components as dbc

FOOTER = html.Footer([
                    dbc.Container([dbc.Row(
                            dbc.Container([
                                dbc.Col(dbc.CardImg(src="/static/bclogoerbostrans.svg", top=True))
                            ], className='col-7 col-sm-7 col-md-7 col-lg-11 col-xl-11')),
                            html.Hr(),
                            dbc.Row(
                            [dbc.Col(
                                [
                                    dbc.NavLink("Contact", href="/contact", className='footer-link'),
                                    dbc.NavLink("FAQ", href="/faq", className='footer-link'),
                                    dbc.NavLink("People", href="/people", className='footer-link'),
                                ], xs=12, sm=12, md=4, lg=4, xl=4),
                                dbc.Col(
                            [
                             dbc.NavLink("Terms of Use", href="/terms", className='footer-link'),
                             dbc.NavLink("Privacy Policy", href="/privacy", className='footer-link'),
                             dbc.NavLink("Accessibility", href="/accessibility", className='footer-link'),
                            ],
                                xs=12, sm=12, md=4, lg=4, xl=4)]),
                     html.Hr(className='my-4')
    ], fluid=True, className='px-0')],
    style={
        'width': '120%',
        'margin-left': '-10%',
        'margin-top': '3%',
        'height': 'auto',
        'background-image': 'linear-gradient(to top, #8624ff, #270850, #13002a)',
        'color': 'white',
        'justify': 'left',
    },
    className='text-center'
)


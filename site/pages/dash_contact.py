from dash import html
import dash_bootstrap_components as dbc


envelope = html.Center(html.Img(src='/static/envelope.svg', height='200px', width='300px'))
toggle_button_blob = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Button(envelope,
                           id="open-modal", className="shape", n_clicks=0, style={'color': 'white',
                                                                                             'font-family': 'Akron',
                                                                                             'font-size': '70px'})),
                 ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
    ], id="open-modal", className="col-xs-12 col-sm-12 col-md-9 col-lg-5 col-xl-5")


main_modal = dbc.Modal([
        dbc.ModalHeader("Contact Us"),
        dbc.ModalBody([
            dbc.Form([
                dbc.Input(id="name", placeholder="Your name", type="text"),
                dbc.Input(id="email", placeholder="Your email", type="email"),
                dbc.Textarea(id="message", placeholder="Your message"),
                html.P(id="output", style={"color": "white"})
            ]),
            dbc.ModalFooter([
                dbc.Button("Close", id="close-modal", className="ml-auto", n_clicks=0, color="secondary"),
                dbc.Button("Submit", id="submit-button", className="ml-2", n_clicks=0, color="secondary")])])
        ], id="modal")

modal_alerts = dbc.Modal([
        dbc.Alert("Something wasn't filled out correctly!", id='error-alert', color="danger", is_open=False),
        dbc.ModalBody(id='verify-modal-body'),
        dbc.ModalFooter(dbc.Button("Close", id="close-verify-modal", className="ml-auto"))
    ], id="verify-modal")


contact = dbc.Container([
    html.Hr(),
    html.Center(html.H1('All Non Subscription Inquiries May Use This Form', className='mb-12', style={'color': 'white',
                                                                                          'font-family': 'Aotani'}, )),
    toggle_button_blob,
    html.Br(),
    html.Center(html.H2('By using this form you consent to being responded to via email.', className='mb-12', style={'color': 'white',
                                                                                          'font-family': 'Aotani'}, )),
    html.Br(),
    main_modal,
    modal_alerts,

], fluid=True)


header = dbc.Container([
        dbc.Col([
            html.Div(style={
              'backgroundImage': 'url("/static/wiredbrain28.svg")',
              'backgroundSize': 'cover',
              'backgroundPosition': 'center 55%',
              'width': '100%',
              'height': '40vh',
              'display': 'flex',
              'alignItems': 'left',
              'justifyContent': 'left'})
            ],
            className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
    ], style={'width': '100%'})


CONTACT = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Contact', className='mb-12', style={'color': 'white',
                                                         'font-size': '50px',
                                                         'font-family': 'Triad'}),
            html.Hr()])]),
    header,
    contact,

])

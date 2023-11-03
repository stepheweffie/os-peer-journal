import dash_bootstrap_components as dbc
from dash import html

contact_form = html.Div([
    dbc.Button("Contact Sales", id="subscribe-collapse-button", className="mb-3", size="lg", color="primary",
               n_clicks=0),
    dbc.Collapse(
        dbc.Form([
            dbc.Container([
                dbc.Row([
                    dbc.Container([
                        dbc.Alert("All fields must be filled!", id='collapse-info-alert', color="info",
                                  is_open=False),
                        dbc.Alert("Thank you for your message. Please verify your email to send this form.",
                                  id='collapse-success-alert', color="dark", is_open=False),
                        dbc.Alert("Please provide a valid phone number!", id='collapse-phone-alert', color="danger",
                                  is_open=False),
                        dbc.Alert("Please provide a valid email address!", id='collapse-email-alert', color="secondary",
                                  is_open=False),
                        dbc.Label("For More Information About Subscriptions", className="mr-2"),

                        dbc.Col(dbc.Input(type="text", id="name-input", placeholder="First Name", required=True,
                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
                    dbc.Container([
                        dbc.Col(dbc.Input(type="text", id='last-name-input', placeholder="Last Name", required=True,
                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8"),
                dbc.Row([
                    dbc.Container([
                        dbc.Col(dbc.Input(type="text", id="institution-input", placeholder="Institution", required=True,
                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
                    dbc.Container([
                        dbc.Col(dbc.Input(type="tel", id="phone-input", placeholder="Phone Number",
                                          inputmode="tel", minlength="7", maxlength="14", required=True,

                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8"),
                dbc.Row([
                    dbc.Container([
                        dbc.Col(dbc.Input(type="email", id="contact-email-input", placeholder="Email",
                                inputmode="email", minlength=6, maxlength=30,required=True,
                        ))], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8"),
                html.Br(),
                dbc.Col(dbc.Textarea(id="subscribe-contact-message", placeholder="Message", size="lg", required=True,
                        rows=5, spellcheck=True, minlength=50, maxlength=500,
                        style={'verticalAlign': 'top'},
                        className="col-xs-12 col-sm-12 col-md-10 col-lg-10 col-xl-10")),
                dbc.Row([
                    dbc.Col(dbc.Button("Submit", id="subscribe-contact-button", n_clicks=0, className="mt-3",
                        size="lg", color="primary"),
                        className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
                    dbc.Col(html.Div(id="subscribe-contact-output", className="mt-3")),
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-8 col-xl-8"),
                ]),
        ]),
        id="subscribe-collapse", is_open=False)
], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-8")

email_input = dbc.Form([
    html.H2("Stay In The Knowledge."),
    dbc.Label("We Won't Forget To Update You When An Article Is Published", className="mr-2"),
    dbc.Col([
        dbc.Input(type="text", id="username-updates-input", placeholder="Enter Name"),
    ], width=6, className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
    dbc.Col([
        html.Div([
            dbc.Input(id="email-input", type="text", placeholder="Email Address", value=""),
            dbc.FormFeedback("Please provide email...", type="invalid"),
            dbc.FormFeedback("That looks like an email address :-)", type="valid"),
            dbc.FormFeedback(
                "Sorry, email invalid...",
                type="invalid",
            ),
        ]),
        dbc.Button("Submit", id="email-updates-button", className="mt-3", color="dark", n_clicks=0),
        html.Br(),
    ], width=6, className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'}),
], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'width': '100%'})


email_toast = dbc.Container([
    dbc.Toast(
        dbc.Container([
            dbc.Alert("Please provide your info.", id="invalid-info-alert", is_open=False, color="danger"),
            dbc.Alert("Thanks for subscribing! Check your email.", id="check-email-alert", is_open=False,
                      color="primary"),
            email_input], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12",
            style={'width': '100%', "color": "white"}),
        header_style={"background-color": "black", "color": "white"},
        dismissable=False,
        is_open=True,
        style={"background-color": "black", "color": "white", "font-family": "Aotani", "width": "100%", "margin-bottom": "13px"},
        className='block')
])
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

EXCLUDED_STATES = ['Alabama', 'Arizona', 'Arkansas', 'Georgia', 'Florida', 'Idaho', 'Indiana', 'Louisiana', 'Kentucky',
                   'Mississippi', 'Missouri', 'Nebraska', 'North Carolina', 'North Dakota', 'Oklahoma', 'South Carolina',
                   'South Dakota', 'Tennessee', 'Texas', 'Utah', 'West Virginia', 'Wisconsin']

all_states = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
              'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
              'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
              'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
              'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
              'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
              'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
              'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
              'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
              'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

cookie_offcanvas = dbc.Offcanvas(
        [
            html.H4("Cookie Consent", className="offcanvas-header"),
            html.Div("Do you accept our private non-shared cookies to improve your app experience?",
                     className="offcanvas-body"),
            dbc.Button("Accept", id="accept-button", color="success", className="me-2", n_clicks=0),
            dbc.Button("Reject", id="reject-button", color="danger", className="me-2", n_clicks=0),
        ],
        id="cookie-consent-offcanvas",
        title="",
        is_open=False,
        close_button=True,
        backdrop=True,
    )


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
        style={"background-color": "black", "color": "white", "width": "100%", "margin-bottom": "13px"},
        className='block')
])

toast0 = dbc.Container([
    dbc.Toast(
        [html.H3('Welcome to Research.', className="ml-2 mb-0"),
            html.H2("Science on the very edge.", className="ml-2 mb-0"),
            html.H2("In a post P vs NP world.", className="ml-2 mb-0"),
            html.H2("Reverse engineering the brain.", className="ml-2 mb-0"),
            ],
        header_style={"background-color": "black", "color": "white", "width": "100%"},
        dismissable=False,
        is_open=True,
        style={"background-color": "black", "color": "white", "width": "100%", "margin-bottom": "13px"},
    ),
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")


toast01 = dbc.Container([
    dbc.Toast(
        [html.H3("Let's Prove Ourselves.", className="ml-2 mb-0"),
            html.H2("New Complexity.", className="ml-2 mb-0"),
            html.H2("Improved Logic.", className="ml-2 mb-0"),
            html.H2("The Gateway To Cognition.", className="ml-2 mb-0"),
            ],
        header_style={"background-color": "black", "color": "white", "width": "100%"},
        dismissable=False,
        is_open=True,
        style={"background-color": "black", "color": "white", "width": "100%", "margin-bottom": "13px"},
    ),
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")


toast1 = dbc.Toast(
    [html.H2('Welcome to the Journal Without Walls.', className="mb-0"),
     html.H1("A Brand New Journal Experience.", className="mb-0"),
     html.H1("Read Freely.", className="mb-0"),
     html.H1("Cite Responsibly.", className="mb-0"),
     ],
    header_style={"background-color": "black", "color": "white", "width": "100%"},
    dismissable=False,
    is_open=True,
    style={"background-color": "black", "color": "white", "width": "100%"},)


placeholder = html.Div([
        dbc.Placeholder(button=True, size='lg', color='black', loading_state=False,
                        className="w-100"),
    ])


toast2 = dbc.Toast(
    [html.H3('Researchers never have to login to read published articles and notebooks.', className="mb-0"),
     html.Br(),
     html.H1("Access The Cutting Edge.", className="mb-0"),
     html.H1("Publish In Jupyter or PDF.", className="mb-0"),
     html.H1("Never Pay To Have Your Work Recognized.", className="mb-0"),
     html.H1("Get Paid To Review And Write.", className="mb-0")],
    header_style={"background-color": "white", "color": "white", "width": "100%"},
    dismissable=False,
    is_open=True,
    style={"background-color": "white", "color": "black", "width": "100%"},)


carousel = dbc.Container(
            dbc.Carousel(items=[
                {"key": "1", "src": "/static/slide1.svg",
                    "header": "A New Kind of Academic Journal",
                    "caption": "On The Cutting Edge of Science"},
                {"key": "2", "src": "/static/wiredbrain24.svg",
                    "header": "Free To Read Forever",
                    "caption": "Eligible Institutions and Businesses Must Subscribe"},
                {"key": "3", "src": "/static/slide3.svg",
                    "header": "Citations Must Be Supported By A Subscription",
                    "caption": "Individuals May Be Eligible For A Free Subscription"},
                                ],
                interval=3600,
                ride="carousel",
                className="carousel-fade",))


def update_map():
    fig = go.Figure()
    # Generate hover text
    hover_text = [f"State: {state}<br>Status: {'Excluded' if state in EXCLUDED_STATES else 'Included'}"
                  for state in all_states.keys()]

    # Define a custom color scale
    colorscale = [
        [0, 'rgba(0, 0, 0, .9)'],  # Included color
        [1, 'rgba(255, 255, 255, 0.9)']  # Excluded color
    ]

    # Add Choropleth map layer
    fig.add_trace(
        go.Choropleth(
            z=[0 if state not in EXCLUDED_STATES else 1 for state in all_states.keys()],
            geojson="https://raw.githubusercontent.com/python-visualization/folium/master/tests/us-states.json",
            locations=list(all_states.values()),  # Using the 2-letter state abbreviations
            locationmode="USA-states",
            colorscale=colorscale,
            showscale=False,
            hoverinfo="text",
            text=hover_text,  # Use the generated hover text
            marker_line_color='whitesmoke',  # Lines between states
        )
    )

    # Update layout for a cleaner look and responsiveness
    fig.update_layout(
        geo=dict(
            scope='usa',
            showland=True,
            landcolor="rgb(200, 200, 200)",
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)",
            showlakes=True,
            lakecolor="rgb(255, 255, 255)",
            showsubunits=True,
        ),
        title_text="",
        title_x=0.5,  # Center the title
        autosize=True,
        margin=dict(t=40, b=40, l=4, r=4),
        paper_bgcolor="black",
    )
    return fig

BODY = html.Div([

        dbc.Container([
            dbc.Row([
                dbc.Container([
                    dbc.Col([
                        html.H1("An Academic Journal That Makes Sense", className="mb-0", style={'color': 'white',
                                                                                  'font-size': '100px'}),
                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12"),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 mt-30", style={'max-width': '100%'}),
                dbc.Container([
                    dbc.Col([
                        dbc.CardImg(src='/static/wiredbrain20.svg', className="mb-10", style={'width': '100%'}),
                    ], className="col-xs-12 col-sm-12 col-md-7 col-lg-12 col-xl-12",
                        style={'max-width': '100%'}),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 mb-10", style={'max-width': '100%'}),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),

            dbc.Container([
                html.Br(),
                dbc.Row([
                    dbc.Container([
                        dbc.Col([
                            toast0,
                            toast01,
                        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
                    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'max-width': '100%'}),
                    dbc.Container([
                        dbc.Col([
                            email_toast,
                        ], className="col-xs-12 col-sm-12 col-md-7 col-lg-12 col-xl-12",
                            style={'max-width': '100%'}),
                        dbc.Col([
                            dbc.Alert("Please, verify to receive updates.", id="email-under-alert", is_open=False, color="primary"),
                        ], className="col-xs-11 col-sm-11 col-md-11 col-lg-11 col-xl-11",
                            style={'max-width': '100%', 'margin-left': '20px', 'margin-right': 'auto'}),

                ], className="col-xs-12 col-sm-12 col-md-12 col-lg-6 col-xl-6", style={'max-width': '100%'}),
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 mt-15", style={'max-width': '100%'})
        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),
        ]),
        dbc.Container([
            placeholder,
            cookie_offcanvas,
            toast2,
            placeholder,
            toast1,
            placeholder,
            ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-width': '100%'}),])

sine_waves = dbc.Container([
        dcc.Graph(id='animated-graph')
    ],)

map_body = html.Div([
    dcc.Interval(
        id='graph-update',
        interval=100,  # Update every 100 ms
        ),
    html.H1("Entities in These States May Subscribe", style={'textAlign': 'center', 'color': 'white',
                                                             'font-size': '66px'}),
    dbc.Container([
        dcc.Graph(id="us-map", figure=update_map()),
        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-height': '80%'}),
])




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
            dbc.Button("Accept", id="accept-button", color="success", className="me-2"),
            dbc.Button("Reject", id="reject-button", color="danger", className="me-2"),
        ],
        id="cookie-consent-offcanvas",
        title="",
        is_open=True,
        backdrop=True,
    )


email_input = dbc.Form([
    html.H2("Stay In The Know.", className="mt-3"),
    dbc.Label("We Won't Forget To Update You When An Article Is Published", className="mr-2"),
    dbc.Row([
        dbc.Col([
            dbc.Input(type="text", id="username-updates--input", placeholder="Enter A Name You Use"),
            dbc.Button("Submit", id="email-button", className="mt-3", color="primary"),
        ], width=6, className="mr-3"),
        dbc.Col([
            dbc.Input(type="email", id="email-updates--input", placeholder="Enter Your Email Address"),
            html.H3("Confirm Your Email For The Most Updated Information.", className="mt-3"),
        ], width=6, className="mr-3"),
    ]),
    html.Div(id="email-output",  style={"width": "6"}, className="mt-3"),
])

card1 = dbc.Card(
    [
        dbc.CardImg(src="/static/logo.svg", top=True),
        dbc.CardBody(
            [
                email_input
            ]
        ),
    ],
    style={"width": '100%'},
)

toast1 = dbc.Toast(
    [html.H2('Welcome to the Journal Without Walls.', className="mb-0"),
     html.H1("A Brand New Journal Experience.", className="mb-0"),
     html.H1("Read Freely.", className="mb-0"),
     html.H1("Cite Responsibly.", className="mb-0"),
     ],
    header="",
    dismissable=False,
    is_open=True,
    style={"background-color": "#ffc107", "color": "black", "width": "100%"},

)


placeholder = html.Div(
    [
        dbc.Placeholder(button=True, size='lg', color='dark', loading_state=False,
                        className="w-100"),
        dbc.Placeholder(button=True,size='lg', color='primary', loading_state=False, className="w-100"),
    ]
)

toast2 = dbc.Toast(
    [html.H3('Researchers never have to login to read published articles and notebooks.', className="mb-0"),
     html.Br(),
     html.H1("Access The Cutting Edge.", className="mb-0"),
     html.H1("Publish In Jupyter or PDF.", className="mb-0"),
     html.H1("Never Pay To Have Your Work Recognized.", className="mb-0"),
     html.H1("Get Paid To Review And Write.", className="mb-0")],
    header="",
    dismissable=False,
    is_open=True,
    style={"background-color": "white", "color": "black", "width": "100%"},

)

carousel = dbc.Container(
            dbc.Carousel(items=[
                {"key": "1", "src": "/static/slide1.svg",
                    "header": "A New Kind of Academic Journal",
                    "caption": "On The Cutting Edge of Science"},
                {"key": "2", "src": "/static/slide2.svg",
                    "header": "Free To Read Forever",
                    "caption": "Eligible Institutions and Businesses Must Subscribe"},
                {"key": "3", "src": "/static/slide3.svg",
                    "header": "Citations Must Be Supported By A Subscription",
                    "caption": "Individuals May Be Eligible For A Free Subscription"},
                                ],
                interval=3600,
                ride="carousel",
                className="carousel-fade",))

contact_form = dbc.Form([
    dbc.Container([
        dbc.Label("For More Information About Subscribing", className="mr-2"),
        dbc.Row([
            dbc.Col([
                dbc.Input(type="text", id="name-input", placeholder="First Name", className="mt-2"),
                    ]),
            dbc.Col([
                dbc.Input(type="text", id='last-name-input', placeholder="Last Name", className="mt-2"),
                    ])
                ]),
        dbc.Row([
            dbc.Col([
                dbc.Input(type="text", id="institution-input", placeholder="Institution", className="mt-2"),
                ]),
            dbc.Col([
                dbc.Input(type="text", id="phone-input", placeholder="Phone Number", className="mt-2"),
                ])
            ]),
        dbc.Row([
            dbc.Col([
                dbc.Input(type="email", id="contact-email-input", placeholder="Email", className="mt-2"),
                    ]),
            dbc.Col([
                dbc.Button("Submit", id="contact-button", className="mt-3", color="primary"),
                    ])
                ]),
    ]),
    html.Div(id="contact-output")
])


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
            marker_line_color='white',  # Lines between states
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
        title_text="For Computer and Brain Science Programs in the US",
        title_x=0.5,  # Center the title
        autosize=True,
        margin=dict(t=40, b=40, l=40, r=40),
        paper_bgcolor="white"
    )
    return fig


BODY = html.Div([
        dbc.Container([card1,
                html.Br(),
            ]),
        carousel,
        dbc.Container(
            toast1
        ),
        placeholder,
        html.H2("States in black respect abortion rights.", style={'textAlign': 'center'}),
        html.H1("Subscription Eligible States", style={'textAlign': 'center'}),
        dcc.Graph(id="us-map", style={'height': '85vh'}, figure=update_map()),
        toast2,
        html.H1('Contact Sales', style={'textAlign': 'center'}),
        contact_form,
        cookie_offcanvas,
        ])

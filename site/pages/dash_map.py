import plotly.graph_objects as go
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


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
        autosize=True,
        margin=dict(t=4, b=4, l=4, r=4),
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode='closest',
        showlegend=False,
    )
    return fig


map_body = html.Div([
    dcc.Interval(
        id='graph-update',
        interval=100,  # Update every 100 ms
        ),
    html.Br(),
    html.H1("Entities in These States May Subscribe", style={'textAlign': 'center',
                                                             'color': 'whitesmoke',
                                                             'font-family': 'Aotani',
                                                             'margin-bottom': '-10px',
                                                           }),
    dbc.Container([
        dcc.Graph(id="us-map", figure=update_map()),
        html.Hr(),
        ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'max-height': '100%'}),
])

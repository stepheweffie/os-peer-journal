from dash import html
import dash_bootstrap_components as dbc


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
        style={"background-color": "black", "color": "white", "width": "100%", "margin-top": "13px",
               "margin-bottom": "13px",
               "font-family": "Aotani"},
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
        style={"background-color": "black", "color": "white", "width": "100%", "margin-bottom": "13px",
               "font-family": "Aotani"},
    ),
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12")


toast1 = dbc.Container([
    dbc.Toast(
    [html.H2('A Journal Without Walls.', className="mb-0"),
     html.H1("An Academic Revolution.", className="mb-0"),
     html.H1("Read Freely.", className="mb-0"),
     html.H1("Cite Responsibly.", className="mb-0"),
     ],
        header_style={"background-color": "black", "color": "white", "width": "100%"},
        dismissable=False,
        is_open=True,
        style={"background-color": "black", "color": "white", "width": "100%", "font-family": "Aotani"},)
    ], className="col-xs-12 col-sm-12 col-md-12 col-lg-12 col-xl-12", style={'margin-bottom': '13px'})


placeholder = html.Div([
        dbc.Placeholder(button=True, size='lg', color='black', loading_state=False,
                        className="w-100"),
    ])


toast2 = dbc.Toast(
    [html.H3('You Have Access.', className="mb-0"),
     html.Br(),
     html.H1("Use It To Discover.", className="mb-0"),
     html.H1("Solve Problems.", className="mb-0"),
     html.H1("Theorize Accurately.", className="mb-0"),
     html.H1("For Humans, By Humans.", className="mb-0")],
    header_style={"background-color": "#aab1ff", "color": "black", "width": "100%"},
    dismissable=False,
    is_open=True,
    style={"background-color": "#aab1ff", "color": "black", "font-family": "Aotani", "width": "100%"},)


toast3 = dbc.Toast(
    [html.H3('Researchers never have to login to read published articles and notebooks.', className="mb-0"),
        html.Br(),
        html.H3("Access The Edge of Science.", className="mb-0"),
        html.H3("Publish In Jupyter or PDF.", className="mb-0"),
        html.H3("Never Pay To Have Your Work Recognized.", className="mb-0"),
        html.H3("Get Paid To Review And Write.", className="mb-0")],
    header_style={"background-color": "#aab1ff", "color": "black", "width": "100%"},
    dismissable=False,
    is_open=True,
    style={"background-color": "#aab1ff",
           "color": "white",
           "font-family": "Aotani",
           "width": "90%",
           'margin-top': '30px',
           'margin-bottom': '30px',
           'padding': '5px'},)


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


toast1 = dbc.Toast(
    [html.H2('Welcome to the Journal Without Walls.', className="mb-0"),
     html.H1("A Brand New Journal Experience.", className="mb-0"),
     html.H1("Read Freely.", className="mb-0"),
     html.H1("Cite Responsibly.", className="mb-0"),
     ],
    header_style={"background-color": "black", "color": "white", "width": "100%"},
    dismissable=False,
    is_open=True,
    style={"background-color": "black", "color": "white", "width": "100%", "font-family": "Aotani"},)


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
    style={"background-color": "white", "color": "black", "font-family": "Aotani", "width": "100%"},)

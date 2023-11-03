import dash_bootstrap_components as dbc
from dash import html


cookie_offcanvas = dbc.Offcanvas([
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
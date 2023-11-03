from dash import html
import dash_bootstrap_components as dbc

COVER = dbc.Container([
    dbc.Container([
        html.Video(
            src='/static/neurotravels.mp4',
            autoPlay=True,
            loop=True,
            muted=True,
            style={
                'position': 'absolute',
                'width': '100%',
                'left': 0,
                'top': 0,
                'height': '100%',
                'objectFit': 'cover',
                'zIndex': 1
        })])])

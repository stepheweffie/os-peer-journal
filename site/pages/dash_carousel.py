from dash import html
import dash_bootstrap_components as dbc

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

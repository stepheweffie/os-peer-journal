from dash import html
import dash_bootstrap_components as dbc

reads = dict()
reads['Article 1'] = 'Article 1 blurb goes here.'
reads['Article 2'] = 'Article 2 blurb goes here.'
articles = [article for article in reads]
read = html.Div([
    dbc.Container([
        articles
])
])
# Read the files wherever the text is located
about_text = 'more about it'
about = html.Div([
        about_text
])

people_text = 'more people stuff'
people = html.Div([
    dbc.Container([
        html.P('People information is listed here.'),
        people_text
])
])

faq_text = 'more faq stuff'
faq = html.Div([
    dbc.Container([
        html.P('FAQ information is listed here.'),
        faq_text
])
])

contact_text = 'more contact stuff'
contact = html.Div([
    dbc.Container([
        html.P('Contact information is listed here.'),
        contact_text
])
])

terms_text = 'more terms stuff'
terms = html.Div([
    dbc.Container([
        html.P('Terms information is listed here.'),
        terms_text
])
])

privacy_text = 'more privacy stuff'
privacy = html.Div([
    dbc.Container([
        html.P('Privacy information is listed here.'),
        privacy_text
])
])

subscribe_text = 'more subscribe stuff'
subscribe = html.Div([
    dbc.Container([
        html.P('Subscribe information is listed here.'),
        subscribe_text
])
])

login_text = 'more login stuff'
login = html.Div([
    dbc.Container([
        html.P('Login information is listed here.'),
        login_text
])
])

logout_text = 'more logout stuff'
logout = html.Div([
    dbc.Container([
        html.P('Logout information is listed here.'),
        logout_text
])
])

register_text = 'more register stuff'
register = html.Div([
    dbc.Container([
        html.P('Register information is listed here.'),
        register_text
])
])

content = [read, about, people, faq, contact, terms, privacy, subscribe, login, logout, register]
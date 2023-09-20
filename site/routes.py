from templates.pages import content
from dash import html

content = content
contents = [[html.Div(c)] for c in content]
page_vars = ['READ', 'ABOUT', 'PEOPLE', 'FAQ', 'CONTACT', 'TERMS', 'PRIVACY', 'SUBSCRIBE', 'LOGIN', 'LOGOUT', 'REGISTER']
pages = []
paths = [v.lower() for v in page_vars]
print(paths)
for p in paths:
    capitalized_name = p.capitalize()
    pages.append([html.Div([[html.H1(f'{capitalized_name}')]])])
    p_empty = p.replace(' ', ' ')
    p_with_slash = "/" + p_empty
    # paths.pop(0)
    print(p_with_slash)
assert len(pages) == len(page_vars)
for l1, l2 in zip(pages, contents):
    l1.extend(l2)
print(pages)
# PAGES = zip(page_vars, pages)

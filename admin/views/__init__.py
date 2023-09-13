from pywebio.platform.flask import webio_view
from pywebio_logic import password_set, register, root, verify_email, journal_app, pywebio_logic_blueprint


pywebio_logic_blueprint.add_url_rule('/', 'logicio', webio_view(root), methods=['GET', 'POST'])
pywebio_logic_blueprint.add_url_rule('/set_password', 'password_set', webio_view(password_set),
                                         methods=['GET', 'POST'])
pywebio_logic_blueprint.add_url_rule('/register', 'register', webio_view(register), methods=['GET', 'POST'])
pywebio_logic_blueprint.add_url_rule('/verify_email', 'verify_email', webio_view(verify_email),
                                         methods=['GET', 'POST'])
pywebio_logic_blueprint.add_url_rule('/exchange', 'exchange', webio_view(journal_app), methods=['GET', 'POST'])

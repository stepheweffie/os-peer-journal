import random
import string
import cherrypy
import bcrypt
from .models import Subscriber


class StringGenerator(object):
    @cherrypy.expose
    def index(self, subscriber=None):
        secret = ''.join(random.sample(string.hexdigits, 6))
        cherrypy.session['secret'] = secret
        cherrypy.session['subscriber'] = subscriber
        user = Subscriber.query.filter_by(verify_code=subscriber).first()
        email = user.email
        name = user.name
        # Send an email with the code and link
        email_text = f'Hi, {name}. Your code is: {secret}'
        hash_secret = bcrypt.hashpw(secret.encode('utf-8'), bcrypt.gensalt())
        link = f'http://127.0.0.1:8080/confirm?code={hash_secret}'
        message = f'{email_text} Button with {link}'
        # send(email_text, link)
        login_url = "http://127.0.0.1:5000/subscriber/login"
        raise cherrypy.HTTPRedirect(login_url)
        # return f'Please check your {subscriber} for a confirmation link: {link} to {secret}'

    @cherrypy.expose
    def confirm(self, code):
        session_code = cherrypy.session.get('secret')
        user = cherrypy.session.get('subscriber')
        if cherrypy.request.method == 'POST':
            if code == session_code:
                dash_success_url = f"http://127.0.0.1:5000/subscriber/confirm?subscriber={user}"
                raise cherrypy.HTTPRedirect(dash_success_url)
            else:
                # Redirect to the login page in the Dash app
                dash_login_url = "http://127.0.0.1:5000/subscriber/login"
                raise cherrypy.HTTPRedirect(dash_login_url)
        else:
            return """<html>
                        <body>
                            <form method="post" action="/confirm">
                                <label for="code">Enter verification code:</label>
                                <input type="text" id="code" name="code">
                                <input type="submit" value="Submit">
                            </form>
                        </body>
                      </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)

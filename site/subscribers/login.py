import random
import string
import cherrypy
import bcrypt
from verify import send_verify_email


class Verification(object):
    @cherrypy.expose
    def index(self, subscriber):
        secret = ''.join(random.sample(string.hexdigits, 6))
        cherrypy.session['secret'] = secret
        cherrypy.session['subscriber'] = subscriber
        email_text = f'Your code is: {secret}'
        hash_secret = bcrypt.hashpw(secret.encode('utf-8'), bcrypt.gensalt())
        link = f'http://127.0.0.1:8080/confirm?code={hash_secret}'
        message = f'{email_text} Button with {link}'
        send_verify_email(subscriber, message)
        # confirm_url = f"http://127.0.0.1:8080/confirm?code={secret}"
        # raise cherrypy.HTTPRedirect(confirm_url)

    @cherrypy.expose
    def confirm(self, code):
        session_code = cherrypy.session.get('secret')
        user = cherrypy.session.get('subscriber')
        if cherrypy.request.method == 'POST':
            if code == session_code:
                dash_success_url = f"http://127.0.0.1:5000/subscriber/confirm?subscriber={user}"
                raise cherrypy.HTTPRedirect(dash_success_url)
            return f'Incorrect code. Please try again.'
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
    cherrypy.quickstart(Verification(), '/', conf)

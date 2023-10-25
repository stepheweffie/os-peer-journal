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
        hash_secret = bcrypt.hashpw(secret.encode('utf-8'), bcrypt.gensalt())
        confirm_url = f"http://127.0.0.1:8080/confirm?code={hash_secret}"
        # cheat_url = f'http://127.0.0.1:8080/confirm?code={secret}'
        send_verify_email(secret, confirm_url, subscriber)

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
         <head>
         <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
        <script defer src="https://pyscript.net/latest/pyscript.js"></script>
            </head>
                <body>
                        <form method="post" action="/confirm">
                            <label for="code">Enter verification code:</label>
                            <input type="text" id="code" name="code">
                            <input type="submit" value="Submit">
                        </form>
                    <py-config>
                plugins = [
                  "https://pyscript.net/latest/plugins/python/py_tutor.py"
                ]
            </py-config>

            <section class="pyscript">
                <py-script>
                 
                </py-script>
            </section>
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

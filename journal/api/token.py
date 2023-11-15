import os
import cherrypy
import random
import string

template_path = 'templates/base.html'


class RESTGeneratorWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        category_string = cherrypy.session.get('session_string')  # Using .get() to handle missing key gracefully
        if category_string is not None:
            return category_string
        else:
            return "Key 'session_string' not found in the session!"

    def POST(self):
        some_string = self.GET()
        cherrypy.session['session_string'] = some_string
        return some_string

    def PUT(self, another_string):
        cherrypy.session['session_string'] = another_string

    def DELETE(self):
        cherrypy.session.pop('session_string', None)


class RESTGenerator(object):
    def __init__(self):
        self.generator = RESTGeneratorWebService()

    @cherrypy.expose
    def index(self):
        with open(template_path, 'r') as f:
            return f.read()

    @cherrypy.expose
    def generate(self, length=8):
        # http://127.0.0.1:8080/generate?length=16
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['session_string'] = some_string
        return 'Check your email for a code to verify'

    @cherrypy.expose
    def verify(self, input_string=None):
        # When the form is submitted, 'input_string' will have a value.
        if input_string:
            # Check if the input string matches the stored session string.
            if 'session_string' in cherrypy.session and input_string == cherrypy.session['session_string']:
                # If it matches, redirect to a new route.
                raise cherrypy.HTTPRedirect('/success')
            else:
                # If not, reload the form with an error message.
                return """
                    <h1>Verification failed</h1>
                    <form action="/verify" method="post">
                        <input type="text" name="input_string" placeholder="Enter generated string">
                        <input type="submit" value="Verify">
                    </form>
                    <p>The entered string did not match. Try again.</p>
                    """
        # Render the form when the /verify route is accessed.
        return """
        <h1>Verify generated string</h1>
        <form action="/verify" method="post">
            <input type="text" name="input_string" placeholder="Enter generated string">
            <input type="submit" value="Verify">
        </form>
        """

    @cherrypy.expose
    def success(self):
        # Handle the redirected route after a successful string match.
        return "<h1>Verification succeeded!</h1><p>You've been redirected because the string matched.</p>"


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))

    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'templates'  # Just the relative path from the root.
        }
    }

    cherrypy.tree.mount(RESTGenerator(), '/', config=conf)
    cherrypy.engine.start()
    cherrypy.engine.block()


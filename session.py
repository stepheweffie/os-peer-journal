import random
import string
import cherrypy
import os


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
         <head>
         <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
        <script defer src="https://pyscript.net/latest/pyscript.js"></script>
         </head>
     <body>
       <form method="get" action="generate">
         <input type="text" value="8" name="length" />
             <button type="submit">Give it now!</button>
       </form>
       <py-config>
                plugins = [
                  "https://pyscript.net/latest/plugins/python/py_tutor.py"
                ]
            </py-config>

            <section class="pyscript">
                Hello world! <br>
                This is the current date and time, as computed by Python:
                <py-script>
                    from datetime import datetime
                    now = datetime.now()
                    display(now.strftime("%m/%d/%Y, %H:%M:%S"))
                </py-script>
            </section>
     </body>
   </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        # http://127.0.0.1:8080/generate?length=16
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        return cherrypy.session['mystring']


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)
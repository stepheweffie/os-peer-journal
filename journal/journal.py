from flask import Flask
import cherrypy


def create_app():
    app = Flask(__name__)

    # ... (your app setup code)

    return app


app = create_app()

if __name__ == "__main__":
    # Wrap the Flask app for CherryPy
    d = cherrypy.wsgiserver.WSGIPathInfoDispatcher({'/': app})

    # Define the CherryPy WSGI server
    server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 5000), d)

    try:
        print("Server is starting on http://0.0.0.0:5000/")
        server.start()
    except KeyboardInterrupt:
        print("Server is stopping...")
        server.stop()
        print("Server stopped.")

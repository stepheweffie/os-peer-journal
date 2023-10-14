from flask import Flask
from subscribers.subscribers import subscribers

app = Flask(__name__)

# Register the blog blueprint with the main app
app.register_blueprint(subscribers, url_prefix='/subscriber')

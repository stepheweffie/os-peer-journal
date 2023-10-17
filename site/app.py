from flask import Flask
from subscribers.__init__ import subscribers
from flask_bootstrap import Bootstrap5
from subscribers.config import SQLALCHEMY_DATABASE_URI
from subscribers.models import db, User, Role
from flask_migrate import Migrate
from flask_session import Session
from flask_security import Security, SQLAlchemyUserDatastore
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'secret_key'  # Set the secret key to the same value as the main app
login_manager = LoginManager(app)
# Create a SQLAlchemyUserDatastore
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# Initialize Flask-Security with the app and user_datastore
security = Security(app, user_datastore)
# Register the blog blueprint with the main app
app.register_blueprint(subscribers, url_prefix='/subscriber')
# Configure the database connection URI
bootstrap = Bootstrap5(app)
app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'vapor'
app.config['BOOTSTRAP_FONTAWESOME'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)
migrate = Migrate(app, db)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
# Initialize Flask-Login
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'  # Specify the login view (replace with your login route)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager
import os 
app = Flask(__name__)


app.config['SECRET_KEY'] = '53c489b6e5a330e302256da286791c88'

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

database = SQLAlchemy(app)
migrate = Migrate(app, database)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category= 'alert-info'

bcrypt = Bcrypt(app)


from comunidade import routes

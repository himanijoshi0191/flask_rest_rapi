from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from . import config
app = Flask(__name__, template_folder='/flask_rest_rapi/templates')
app.config.from_object(config)
db = SQLAlchemy()
bcrypt = Bcrypt(app)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

@app.before_first_request
def create_tables():
    from .model import AddNews
    db.create_all()
from . import test
import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .helpers.logger_helper import init_logger

init_logger()
load_dotenv(override=True)

db = SQLAlchemy()


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_DSN"]
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.init_app(app)

from .auth import auth as auth_blueprint  # noqa=E402

app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint  # noqa=E402

app.register_blueprint(main_blueprint)

from .models.user import User  # noqa=E402


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except Exception:
        return None

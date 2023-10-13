from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from sqlalchemy import MetaData
db = SQLAlchemy()
app = Flask(__name__)
app.config["SECRET_KEY"] = "asoigdjsi"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
migrate = Migrate(app, db)
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)


@login_manager.user_loader
def load_user(id):
    from models import User
    return User.query.get(id)

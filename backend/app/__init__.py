# app/__init__.py

from flask import Flask
from .config import Config
from .extensions import db, migrate, ma, bcrypt, jwt, mail
from .routes import register_blueprints

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    # Register routes/blueprints
    register_blueprints(app)

    return app

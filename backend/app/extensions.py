# app/extensions.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
mail = Mail()

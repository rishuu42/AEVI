# app/routes/__init__.py

from flask import Flask
from .auth_routes import auth_bp
from .product_routes import product_bp
from .order_routes import order_bp
from .user_routes import user_bp

def register_blueprints(app: Flask):
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(product_bp, url_prefix="/api/products")
    app.register_blueprint(order_bp, url_prefix="/api/orders")

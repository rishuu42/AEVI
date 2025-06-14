# app/controllers/auth_controller.py

from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.models.user import User
from app.extensions import db, bcrypt
from datetime import timedelta

def signup_user():
    data = request.get_json()

    if not data or not all(k in data for k in ("email", "password", "username")):
        return jsonify({"message": "Missing required fields"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email already registered"}), 409

    hashed_password = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    new_user = User(
        email=data["email"],
        username=data["username"],
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


def login_user():
    data = request.get_json()

    if not data or not all(k in data for k in ("email", "password")):
        return jsonify({"message": "Missing email or password"}), 400

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not bcrypt.check_password_hash(user.password, data["password"]):
        return jsonify({"message": "Invalid email or password"}), 401

    access_token = create_access_token(
        identity=user.id,
        expires_delta=timedelta(hours=24)
    )

    return jsonify({
        "access_token": access_token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 200

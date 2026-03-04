from flask import Blueprint, request, jsonify
from models import User
from extensions import db
from werkzeug.security import generate_password_hash

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.json

    user = User(
        username=data["username"],
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role=data["role"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"})

from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json

    user = User.query.filter_by(email=data["email"]).first()

    if not user:
        return jsonify({"msg": "User not found"}), 404

    if not check_password_hash(user.password, data["password"]):
        return jsonify({"msg": "Invalid password"}), 401

    token = create_access_token(
        identity=user.id,
        additional_claims={"role": user.role}
    )

    return jsonify({"token": token})
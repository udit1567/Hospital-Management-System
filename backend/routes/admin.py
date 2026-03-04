from flask import Blueprint, jsonify
from models import Doctor, Patient
from utils.decorators import role_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/dashboard")
@role_required("admin")
def dashboard():

    doctors = Doctor.query.count()

    patients = Patient.query.count()

    return jsonify({
        "total_doctors": doctors,
        "total_patients": patients
    })
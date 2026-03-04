@patient_bp.route("/book", methods=["POST"])
def book():

    data = request.json

    existing = Appointment.query.filter_by(
        doctor_id=data["doctor_id"],
        date=data["date"],
        time=data["time"]
    ).first()

    if existing:
        return {"msg": "Slot already booked"}, 400

    appointment = Appointment(
        patient_id=data["patient_id"],
        doctor_id=data["doctor_id"],
        date=data["date"],
        time=data["time"]
    )

    db.session.add(appointment)
    db.session.commit()

    return {"msg": "Appointment booked"}
from extensions import db
from datetime import datetime


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)

    password = db.Column(db.String(200))

    role = db.Column(db.String(50))  # admin doctor patient

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Specialization(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Doctor(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    specialization_id = db.Column(
        db.Integer,
        db.ForeignKey('specialization.id')
    )


class Patient(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    age = db.Column(db.Integer)

    phone = db.Column(db.String(20))


class Appointment(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))

    date = db.Column(db.Date)

    time = db.Column(db.String(20))

    status = db.Column(db.String(20), default="booked")


class Treatment(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    appointment_id = db.Column(
        db.Integer,
        db.ForeignKey('appointment.id')
    )

    diagnosis = db.Column(db.Text)

    prescription = db.Column(db.Text)
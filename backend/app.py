from flask import Flask
from config import Config
from extensions import db, jwt, migrate

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    from routes.auth_routes import auth_bp
    from routes.admin_routes import admin_bp
    from routes.doctor_routes import doctor_bp
    from routes.patient_routes import patient_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(patient_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
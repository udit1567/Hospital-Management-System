import os

class Config:
    SECRET_KEY = "super-secret-key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "jwt-secret"

    REDIS_URL = "redis://localhost:6379/0"
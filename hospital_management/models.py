from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=True)

    department = db.relationship("Department", back_populates="doctors")

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    doctors = db.relationship("User", back_populates="department")

class Appointment(db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    time = db.Column(db.String(20))
    status = db.Column(db.String(20), default='Booked')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    treatment_id = db.Column(db.Integer, db.ForeignKey('treatment.id'))  # Removed unique constraint

class Treatment(db.Model):
    __tablename__ = "treatment"

    id = db.Column(db.Integer, primary_key=True)
    treat_name = db.Column(db.String(100))
    description = db.Column(db.Text)

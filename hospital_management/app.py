
from flask import Flask, render_template, redirect, url_for

import sqlite3

from flask import request

from models import db, User, Department, Appointment, Treatment

import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db.init_app(app)

with app.app_context():
    db.create_all()
    existing_admin = User.query.filter_by(username="admin").first()

    if not existing_admin:
        admin_db = User(username="admin",password="admin",email="11d@gmail.com", role="admin")
        db.session.add(admin_db)
        db.session.commit()
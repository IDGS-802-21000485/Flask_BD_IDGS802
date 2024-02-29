from flask_sqlalchemy import SQLAlchemy
import datetime

db=SQLAlchemy()

class alumno(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(50))
    correo=db.Column(db.String(50))
    create_date=db.Column(db.DateTime, default=datetime.datetime.now)
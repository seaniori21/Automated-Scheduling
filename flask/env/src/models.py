from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class Employer(db.Model):
    __tablename__ = 'employers'
    id = db.Column(db.String(11), primary_key=True, unique=True, default =get_uuid)
    email = db.Column(db.String(150), unique=True)
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    password = db.Column(db.Text, nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(11), primary_key=True, unique=True, default =get_uuid)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.Text, nullable=False)
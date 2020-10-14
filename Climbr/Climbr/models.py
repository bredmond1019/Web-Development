import os
from flask_sqlalchemy import SQLAlchemy
from Climbr import db

from werkzeug.security import generate_password_hash, check_password_hash



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)


    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('pasword is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
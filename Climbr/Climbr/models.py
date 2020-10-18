import os
from flask_sqlalchemy import SQLAlchemy
from Climbr import db
from flask_login import UserMixin
from . import login_manager

from werkzeug.security import generate_password_hash, check_password_hash



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # Personal Info
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zip_code = db.Column(db.Integer)

    # Climbing Info
    climbing_gym = db.Column(db.String(20))
    climbing_preference = db.Column(db.String(20))

    # Login Credentials
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('pasword is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)






@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



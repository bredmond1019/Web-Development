import os
from flask_sqlalchemy import SQLAlchemy
from Climbr import db
from flask_login import UserMixin, AnonymousUserMixin
from . import login_manager
from flask import current_app

from datetime import datetime, timezone

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
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
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default = False)

    # Extra Info
    member_since = db.Column(db.DateTime(), default=datetime.now(tz = timezone.utc))
    last_seen = db.Column(db.DateTime(), default=datetime.now(tz = timezone.utc))
    about = db.Column(db.String(300))
    photo_url = db.Column(db.String(200))

    # Role
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['CLIMBR_ADMIN']:
                self.role = Role.query.filter_by(name='Administrator').first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)
    
    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def ping(self):
        self.last_seen = datetime.now(tz = timezone.utc)
        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('pasword is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration = 3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id}).decode('utf-8')
    
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
    
    def __repr__(self):
        return f'<User {self.id}: {self.last_name}, {self.first_name}>'


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions =db.Column(db.Integer)
    users = db.relationship("User", backref = 'role')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0
    
    def __repr__(self):
        return f'<Role {self.id}: {self.name}>'

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm
    
    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm
    
    def reset_permissions(self):
        self.permissions = 0
    
    def has_permission(self, perm):
        return self.permissions & perm == perm

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
            'Moderator': [Permission.FOLLOW, Permission.COMMENT, 
                          Permission.WRITE, Permission.MODERATE],
            'Administrator' : [Permission.FOLLOW, Permission.COMMENT, 
                               Permission.WRITE, Permission.MODERATE,
                               Permission.ADMIN],
        }
        default_role = "User"
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False
    
    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



from enum import unique
from backend import db
from datetime import datetime


client_provider = db.Table('client_provider',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('provider_id', db.Integer, db.ForeignKey('provider.id')),
    db.Column('plan', db.Enum("basic", "premium", name="provider_plan"))
    )


class Provider(db.Model):
    __tablename__ = 'provider'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

    clients = db.relationship("Client", secondary=client_provider, backref='providers')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Provider {self.name}, email: {self.email}>"

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
        return data




class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)

    journal_entries = db.relationship("JournalEntry", backref="client")

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Provider {self.name}, email: {self.email}>"

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'email': self.email, 
            "journal_entries" : self.journal_entries
        }
        return data


class JournalEntry(db.Model):
    __tablename__ = 'journal_entry'
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(5000))
    user_id = db.Column(db.Integer, db.ForeignKey("client.id"))
    date_entered = db.Column(db.DateTime(), default=datetime.now())
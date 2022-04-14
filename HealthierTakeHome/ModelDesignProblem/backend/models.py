from enum import unique
from backend import db
from datetime import datetime



class Provider(db.Model):
    __tablename__ = 'provider'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)


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
        return f"<Client {self.name}, email: {self.email}>"

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'email': self.email, 
            "journal_entries" : [journal_entry.to_dict() for journal_entry in self.journal_entries]
        }
        return data



class Plan(db.Model):
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True)
    plan_type = db.Column(db.Enum("basic", "premium", name="provider_plan"))

    def to_dict(self):
        data = {
            'id': self.id,
            'plan_type': self.plan_type
        }
        return data


    

class ClientProvider(db.Model):
    __tablename__ = "client_provider"
    id = db.Column(db.Integer, primary_key=True)

    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'))
    client_id = db.Column( db.Integer, db.ForeignKey('client.id'))
    plan_id = db.Column( db.Integer, db.ForeignKey('plan.id'))

    client = db.relationship("Client", backref = "client_providers")
    provider = db.relationship("Provider", backref = "client_providers")
    plan = db.relationship("Plan", backref = "client_providers")

    def to_dict(self):
        data = {
            'id': self.id,
            'provider': self.provider.to_dict(),
            'client': self.client.to_dict(), 
            "plan" : self.plan.to_dict()
        }
        return data

    def __repr__(self):
        return f"<ClientProvider -- client: {self.client.name}, provider: {self.provider.name}, plan: {self.plan.plan_type} >"



class JournalEntry(db.Model):
    __tablename__ = 'journal_entry'
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("client.id"))
    date_entered = db.Column(db.DateTime(), default=datetime.now())

    def to_dict(self):
        data = {
            'id': self.id,
            'provider': self.entry,
            'client': self.user_id, 
            "plan" : self.date_entered
        }
        return data


    def __repr__(self):
        return f"<Journal Entry -- user: {self.user_id}, date: {self.date_entered}, text: {self.entry[:10]}>"




# How to import the Flask class
from flask import Flask

# How to import SQLAlchemy 
from flask_sqlalchemy import SQLAlchemy 

# Standard way of creating a flask application
app = Flask(__name__)

# Connect to database using config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flaskpractice:flask@localhost:5432/flaskpractice'
"""NEED TO CHANGE # TO PASSWORD ABOVE!"""

# Turn off Modifications Tracking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Link our database to our app with SQLAlchemy
db = SQLAlchemy(app)


# We can create a class of Person and link it to the db Model
class Person(db.Model):
    # To name the table:
    __tablename__ = 'persons'

    # To create a column we do the following:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Person ID: {self.id}, name: {self.name}"

# Next we actually have to create the db for all the models we have
db.create_all()

# This will link to the homepage route
@app.route('/')
def index():
    person = Person.query.first()
    return f"Hello {person.name}!"

    


'''
To run the app, you need to type to the command line:
    FLASK_APP=<name_of_file> FLASK_Debug=true flask run
'''


'''
To add another person, we can use:
person = Person(name='Felipe')
db.session.add(person)
db.session.commit()
'''











"""
Example: A driver has many vehicles
"""


class Driver(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    state = db.Column(db.String(2), nullable = False)
    issued = db.Column(db.DateTime())
    vehicle = db.relationship("Vehicle", backref = 'drivers', lazy=True)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable = False)
    model = db.Column(db.String(50), nullable = False)
    year = db.Column(db.Integer(4), nullable = False)
    drivers_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable = False)



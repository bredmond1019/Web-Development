from random import randint, choice
from sqlalchemy.exc import IntegrityError, DataError
from faker import Faker

from . import db
from .models import User, Post

from sqlalchemy.exc import SQLAlchemyError

def users(count=100):
    fake = Faker()
    i = 0
    while i < count:
        email = fake.unique.email()
        user = User(first_name = fake.first_name(),
                 last_name = fake.last_name(),
                 age = randint(16, 99),
                 address = fake.street_address(),
                 city = "New York",
                 state = "NY",
                 zip_code = int(fake.postcode()),
                 climbing_gym = choice([
                                'The Cliffs @ LIC',
                                'Brooklyn Boulders Gowanus', 
                                'Brooklyn Boulders Queensborough', 
                                'Central Rock Gym', 
                                'Steep Rock West', 
                                'The Gravity Vault', 
                                'Chelsea Piers', 
                                ]),
                climbing_preference = choice(["Top Rope", "Sport", "Trad"]),
                email = email,
                username = email.split('@')[0],
                password = 'password',
                confirmed = True,
                member_since = fake.past_date(),
                about = fake.text())
        db.session.add(user)
        try:
            db.session.commit()
            i+=1
        except (IntegrityError, DataError):
            # print(e)
            db.session.rollback()
    db.session.close()

def posts(count=50):
    fake = Faker()
    user_count = User.query.count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        p = Post(body=fake.text(),
                 timestamp = fake.past_date(),
                 author = u)
        db.session.add(p)
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
    finally:
        db.session.close()
    


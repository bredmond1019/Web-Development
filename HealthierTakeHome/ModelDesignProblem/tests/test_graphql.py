import unittest
from graphene.test import Client
from flask import current_app

from backend import create_app, db
from backend.models import Wombat
from backend.schema import schema
from datetime import date


class BasicsGraphQLTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = Client(schema)

        db.create_all()
        db.session.add_all([
            Wombat("Alice", date(1865, 11, 26)),
            Wombat("Queen", date(1951, 7, 26)),
            Wombat("Johnny", date(2010, 3, 5))
        ])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        self.client = None

    def test_app_exists(self):
        assert current_app is not None

    def test_app_is_testing(self):
        assert current_app.config['TESTING']
        assert current_app.config['DEBUG']
        assert current_app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///'


class WombatGraphQLTestCase(BasicsGraphQLTestCase):

    def test_get_wombats(self):
        executed = self.client.execute("""
                query Wombats {
                    wombats {
                        name
                        dob
                    }
                }
            """)

        assert executed == {"data": {
            "wombats": [
                {"name": "Johnny", "dob": "2010-03-05"},
                {"name": "Queen", "dob": "1951-07-26"},
                {"name": "Alice", "dob": "1865-11-26"}
            ]}}

    def test_post_wombat(self):
        def post(**kwargs):
            return self.client.execute("""
                    mutation Wombat($name: String!, $dob: Date! ) {
                        mutateWombat(name: $name, dob: $dob) {
                            wombat {
                                name
                                dob
                            }
                        }
                    }
                """, variables=kwargs)

        executed = post()
        assert executed['errors'][0]['message'] == 'Variable "$name" of required type "String!" was not provided.'

        executed = post(name="Charlie")
        assert executed['errors'][0]['message'] == 'Variable "$dob" of required type "Date!" was not provided.'

        executed = post(name="Charlie", dob="2005-11-26")
        assert executed == {"data": {
            "mutateWombat": {
                "wombat": {
                    "name": "Charlie",
                    "dob": "2005-11-26"
                }}}}

        executed = self.client.execute("""
                query Wombats {
                    wombats {
                        name
                        dob
                    }
                }
            """)

        assert executed == {"data": {
            "wombats": [
                {"name": "Johnny", "dob": "2010-03-05"},
                {"name": "Charlie", "dob": "2005-11-26"},
                {"name": "Queen", "dob": "1951-07-26"},
                {"name": "Alice", "dob": "1865-11-26"}
            ]}}

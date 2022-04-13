import unittest
from flask import current_app
from backend import create_app, db
from backend.models import Wombat
from datetime import date


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

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


class WombatTestCase(BasicsTestCase):
    def test_get_wombats(self):
        response = self.client.get('/wombats')
        assert response.status_code == 200
        assert response.headers['content-type'].startswith('application/json')
        assert response.json == {
            "wombats": [
                {"id": 1, "name": "Alice",  "dob": "1865-11-26"},
                {"id": 2, "name": "Queen",  "dob": "1951-07-26"},
                {"id": 3, "name": "Johnny", "dob": "2010-03-05"},
            ],
        }

    def test_post_wombats(self):
        def post(**kwargs):
            return self.client.post('/wombats', data=kwargs)

        response = post()
        assert response.status_code == 400
        assert response.get_data(as_text=True) == 'Missing parameter: name'

        response = post(name='Charlie')
        assert response.status_code == 400, response.text
        assert response.get_data(as_text=True) == 'Missing parameter: dob'

        response = post(name='Charlie', dob='2005-11-26')
        assert response.status_code == 200, response.text
        assert response.headers['content-type'].startswith('application/json')
        assert response.json == {
            "id": 4,
            "name": "Charlie",
            "dob": "2005-11-26"
        }

        response = self.client.get('/wombats')
        assert response.json == {
            "wombats": [
                {"id": 1, "name": "Alice",  "dob": "1865-11-26"},
                {"id": 2, "name": "Queen",  "dob": "1951-07-26"},
                {"id": 3, "name": "Johnny", "dob": "2010-03-05"},
                {"id": 4, "name": "Charlie", "dob": "2005-11-26"}
            ],
        }

    def test_unsupported_methods(self):
        for method in ['PUT', 'PATCH', 'DELETE', 'FARFAGNUGEN']:
            response = self.client.open(method=method)
            assert response.status_code == 405
            assert response.get_data(as_text=True) == "Method Not Allowed"

    def test_get_root(self):
        response = self.client.get("/")
        assert response.headers['content-type'] == 'text/plain'
        assert response.status_code == 200
        assert response.get_data(as_text=True) == 'Inspire Candidate Exercise'

    def test_404(self):
        response = self.client.get("/nowhere")
        assert response.status_code == 404

from backend import create_app, db
from backend.models import Provider, Client, Plan, ClientProvider, JournalEntry
from flask_migrate import Migrate


app = create_app('development')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Provider=Provider, Client=Client, Plan=Plan, ClientProvider=ClientProvider, JournalEntry=JournalEntry)


@app.cli.command()
def test():
    """ Run Unit Tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

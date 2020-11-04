import os
from Climbr import create_app, db
from Climbr.models import User, Role, Permission, Post
from flask_migrate import Migrate


app = create_app('development')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission, Post=Post)
from fala import create_app, db, models
from fala.models import User
from flask_migrate import Migrate




app = create_app('development')
migrate = Migrate(app, db)



@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User = User)

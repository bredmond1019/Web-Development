from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from config import config
from datetime import date


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")

    db.init_app(app)

    if config_name == 'development':
        @app.before_first_request
        def initialize_database():
            from .models import Wombat
            db.create_all()
            db.session.add_all([
                Wombat("Alice", date(1865, 11, 26)),
                Wombat("Queen", date(1951, 7, 26)),
                Wombat("Johnny", date(2010, 3, 5))
            ])
            db.session.commit()

    from .schema import schema

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app

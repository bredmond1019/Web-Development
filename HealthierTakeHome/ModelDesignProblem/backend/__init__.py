from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from config import config

from .database_init import create_database_entries




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
            create_database_entries(db)
        

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

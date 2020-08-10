from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__)

    # Load the default configuration
    app.config.from_object('config.default')

    # Load the configuration from the instance folder
    app.config.from_pyfile('instance/config.py')

    # Load the file specified by the APP_CONFIG_FILE environment variable
    # Variables defined here will override those in the default configuration
    app.config.from_envvar('APP_CONFIG_FILE')

    from . import university, user, database, elastic

    api = Api(app)

    elastic.elastic_init(app)
    database.db_init(app)
    university.init_app(app, api)
    user.init_app(app, api)

    return app

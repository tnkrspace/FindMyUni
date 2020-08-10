from flask_mongoengine import MongoEngine


mongo = MongoEngine()


def db_init(app):
    mongo.init_app(app)

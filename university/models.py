from database import mongo
import mongoengine_goodjson as goodjson
from mongoengine import signals
from elastic.search import add_to_index, remove_from_index


class University(goodjson.Document):
    __searchable__ = ['alpha_two_code', 'country', 'domain', 'name', 'web_page']
    alpha_two_code = mongo.StringField(required=True)
    country = mongo.StringField(required=True)
    domain = mongo.StringField(required=True, unique=True)
    name = mongo.StringField(required=True, unique=True)
    web_page = mongo.StringField(required=True, unique=True)

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        add_to_index(sender.__name__.lower(), document)

    @classmethod
    def post_delete(cls, sender, document, **kwargs):
        remove_from_index(sender.__name__.lower(), document)


signals.post_save.connect(University.post_save, sender=University)
signals.post_delete.connect(University.post_delete, sender=University)

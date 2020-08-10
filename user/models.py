from database import mongo
import mongoengine_goodjson as goodjson
from university.models import University


class User(goodjson.Document):
    email = mongo.EmailField(required=True, unique=True)
    name = mongo.StringField(required=True)
    role = mongo.StringField(required=True, choices=('user', 'admin'), default='user')
    last_login = mongo.DateTimeField(required=True)
    uni_tracker = mongo.ListField(mongo.ReferenceField(University, mongo.PULL))


class UserPassword(goodjson.Document):
    user_id = mongo.ReferenceField(User, reverse_delete_rule=mongo.CASCADE)
    hash = mongo.StringField(required=True)
    last_pass_change = mongo.DateTimeField(required=True)


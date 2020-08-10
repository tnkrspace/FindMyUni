from flask import request, jsonify
from .models import User
from flask_restful import Resource
from datetime import datetime

class UserApi(Resource):
    def get(self, user_id):
        user = User.objects.get(id=user_id).to_json()

        return jsonify(user), 200

    def delete(self, user_id):
        user = User.objects.get(id=user_id).delete()
        user['status'] = 'User Deleted Successfully'

        return jsonify(user), 200


class UserPersistApi(Resource):
    def post(self):
        body = request.get_json()
        for user_obj in body:
            user_obj['last_login'] = datetime.now().utcnow()
            user = User(**user_obj).save()
            user_obj['status'] = 'User Added Successfully'
            user_obj['id'] = user.id
            user_obj['uni_tracker'] = []

        return jsonify(body), 200

    def put(self):
        body = request.get_json()
        for user_obj in body:
            user_id = user_obj.get('id')
            User.objects.get(id=user_id).update(set__email=user_obj.get('email'),
                                                set__name=user_obj.get('name'),
                                                set__uni_tracker=user_obj.get('uni_tracker'))
            user_obj['status'] = 'User Updated Successfully'

        return jsonify(body), 200


class UserRoleApi(Resource):
    def post(self):
        body = request.get_json()
        user_id = body.get('user_id')
        role = body.get('role')
        User.objects.get(id=user_id).update(set__role=role)
        body['status'] = 'User Role Updated'

        return jsonify(body), 200


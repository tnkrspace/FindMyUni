from flask import request, jsonify
from .models import University
from flask_restful import Resource
from elastic.search import query_index


class UniversityApi(Resource):
    def get(self, uni_id):
        uni = University.objects.get(id=uni_id).to_json()

        return jsonify(uni), 200

    def delete(self, uni_id):
        uni = University.objects.get(id=uni_id).delete()
        uni['status'] = 'University Deleted Successfully'

        return jsonify(uni), 200


class UniversityPersistApi(Resource):
    def post(self):
        body = request.get_json()
        for uni_obj in body:
            uni = University(**uni_obj).save()
            uni_obj['status'] = 'University Added Successfully'
            uni_obj['id'] = uni.id

        return jsonify(body), 200

    def put(self):
        body = request.get_json()
        for uni_obj in body:
            uni_id = uni_obj.get('id')
            uni_obj.pop('id', None)
            University.objects.get(id=uni_id).update(**uni_obj)
            uni_obj['status'] = 'University Updated Successfully'
            uni_obj['id'] = uni_id

        return jsonify(body), 200


class UniversitySearchApi(Resource):
    def post(self):
        body = request.get_json()
        uni_list = query_index(str(University), body)

        return jsonify(uni_list), 200


from .university import UniversityApi, UniversityPersistApi, UniversitySearchApi


def route_init(api):
    api.add_resource(UniversityApi, '/api/university/<uni_id>', methods=['GET', 'DELETE'])
    api.add_resource(UniversityPersistApi, '/api/university', methods=['POST', 'PUT'])
    api.add_resource(UniversitySearchApi, '/api/university/search', methods=['POST'])

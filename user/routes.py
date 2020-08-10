from .user import UserApi, UserPersistApi, UserRoleApi


def route_init(api):
    api.add_resource(UserApi, '/api/user/<user_id>', methods=['GET', 'DELETE'])
    api.add_resource(UserPersistApi, '/api/user', methods=['POST', 'PUT'])
    api.add_resource(UserRoleApi, '/api/user/role', methods=['POST'])

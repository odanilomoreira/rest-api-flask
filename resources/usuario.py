from flask_restful import Resource

class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_user(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_user(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        user.delete_user()
        return {'message': 'User deleted.'}, 200

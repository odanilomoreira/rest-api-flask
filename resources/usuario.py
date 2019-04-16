from flask_restful import Resource, reqparse

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

class UserRegister(Resource):

    def post(self):
        atributos = reqparse.RequestParser()
        atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank.")
        atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank.")
        data = atributos.parse_args()

        if UserModel.find_user(data['login']):
            return {"message":"The login '{}' already exists!".format(data['login'])}, 400

        # user = UserModel(data['username'], data['password'])
        user = UserModel(**data)

        user.save_to_db()

        return {"message": "User created successfully!"}, 201

from flask import Blueprint
from flask_restful import Api

from .auth import GenerateTokenResource, LoginApi, LogoutApi
from .post import PostResource, PostsResource
from .user import UsersResource, UserResource

bp = Blueprint('api', __name__, url_prefix="/api")
api = Api(bp)


api.add_resource(UsersResource, '/users', endpoint="users_list")
api.add_resource(UserResource, '/users/<int:user_id>', endpoint="users_details")

api.add_resource(PostResource, '/posts/<int:post_id>', endpoint='post_details')
api.add_resource(PostsResource, '/posts', endpoint='post_list')


api.add_resource(GenerateTokenResource, '/generate-token', endpoint='generate_token')
api.add_resource(LoginApi, '/login', endpoint='login')
api.add_resource(LogoutApi, '/logout', endpoint='logout')
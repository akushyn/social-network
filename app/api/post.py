from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request, jsonify

from app import db
from app.models import Post, Like
from app.schemas import PostSchema, LikeSchema, PostListSchema
from flask_login import current_user


class PostResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, post_id):
        post = db.session.query(Post).filter(Post.id == post_id).first_or_404()
        return jsonify(PostSchema().dump(post, many=False))

    def put(self, post_id):
        json_data = request.get_json()
        json_data['id'] = post_id

        updated_post = PostSchema().load(json_data)
        db.session.add(updated_post)
        db.session.commit()

        return jsonify(PostSchema().dump(updated_post, many=False))

    def delete(self, post_id):
        post = db.session.query(Post).filter(Post.id == post_id).first_or_404()
        db.session.delete(post)
        db.session.commit()

        return jsonify(success=True)


class PostsResource(Resource):
    def get(self):
        author_id = request.args.get('author_id', type=int)

        query = db.session.query(Post)

        if author_id:
            query = query.filter(Post.author_id == author_id)

        # add more query filters
        posts = query.all()

        return jsonify(PostListSchema().dump(posts, many=True))

    def post(self):
        json_data = request.get_json()
        if json_data['author_id'] != current_user.id:
            response = jsonify(error="Post author not match")
            response.status_code = 400
            return response

        new_post = PostSchema().load(json_data)
        return jsonify(PostSchema().dump(new_post, many=False))


class LikesResource(Resource):
    def post(self):
        json_data = request.get_json()

        post_id = json_data['post_id']
        user_id = json_data['user_id']

        like = (
            db.session.query(Like)
            .filter(
                Like.post_id == post_id,
                Like.user_id == user_id
            )
            .first()
        )

        if like:
            response = jsonify(error="Like already set")
            response.status_code = 400

            return response

        new_like = LikeSchema().load(json_data)

        return jsonify(LikeSchema().dump(new_like, many=False))


class BulkLikesResource(Resource):
    def post(self):
        json_data = request.get_json()
        ids = json_data['ids']

        likes = []
        for index, id in enumerate(ids):
            likes.append(Like(user_id=current_user.id, post_id=id))

            if index % 10 == 0:
                db.session.bulk_save_objects(likes)

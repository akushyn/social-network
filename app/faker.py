import click
from flask import Blueprint
from faker import Faker

from app import db
from app.models import User, Post
from app.services import UserService

bp = Blueprint('fake', __name__)
faker = Faker()
user_service = UserService()


@bp.cli.command("users")
@click.argument('num', type=int)
def users(num):
    """
    Create 'num' of fake users
    """
    for i in range(num):
        # generate fake username
        username = faker.user_name()

        # generate fake email
        email = faker.email()

        # get user by username & email
        user = (
            db.session.query(User)
            .filter(
                User.username == username,
                User.email == email
            )
        ).first()

        # no such user in db yet --> insert
        if not user:
            user_service.create(
                username=username,
                email=email,
                password=username
            )

    # persist changes
    db.session.commit()
    print(f'{num} users added.')


@bp.cli.command("user_posts")
@click.argument('user_id', type=int)
@click.argument('num', type=int)
def user_posts(user_id, num):
    """
    Create the given number of fake posts, assigned to random users
    """

    user = user_service.get_by_id(user_id)
    for i in range(num):
        created_at = faker.date_time_this_year()
        post = Post(
            title=f"Post at {str(created_at)}",
            content=faker.paragraph(),
            author=user,
            created_at=created_at
        )
        db.session.add(post)
    db.session.commit()
    print(num, 'posts added.')

from app import db, cache
from app.main import bp
from flask import render_template

from app.models import Post


@bp.route("/")
@bp.route("/index")
def index():

    # cache.clear()
    cache_key = "posts"
    cached_value = cache.get(cache_key)
    if cached_value is not None:
        posts = cached_value

    else:
        posts = db.session.query(Post).order_by(Post.created_at.desc()).all()
        cache.set(cache_key, posts)

    for post in posts:
        db.session.add(post)

    return render_template("index.html", posts=posts)


@bp.route('/about')
def about():
    return render_template("about.html")

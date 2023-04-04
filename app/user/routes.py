from app import db
from app.models import Post
from app.post.forms import PostForm
from app.user import bp
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required

from app.user.forms import ProfileForm


@bp.route("/blog")
def blog():
    """
    Display user posts view
    """
    form = PostForm()
    posts = (
        db.session.query(Post)
            .filter(
            Post.author_id == current_user.id
        )
            .order_by(Post.created_at.desc())
            .all()
    )
    return render_template("user/blog.html", posts=posts, form=form)


@bp.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():

        current_user.profile.first_name = form.first_name.data
        current_user.profile.last_name = form.last_name.data
        current_user.profile.linkedin = form.linkedin.data
        current_user.profile.facebook = form.facebook.data
        current_user.profile.bio = form.bio.data
        db.session.commit()
        flash('Your changes have been saved.', category="success")
        return redirect(url_for('user.profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.profile.first_name
        form.last_name.data = current_user.profile.last_name
        form.linkedin.data = current_user.profile.linkedin
        form.facebook.data = current_user.profile.facebook
        form.bio.data = current_user.profile.bio
    return render_template('user/profile.html', user=current_user, form=form)

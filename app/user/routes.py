from app import db
from app.models import User
from app.user import bp
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required

from app.user.forms import EditProfileForm


@bp.route("/profile")
@login_required
def profile():
    posts = [
        {'author': current_user, 'body': 'Test post #1'},
        {'author': current_user, 'body': 'Test post #2'}
    ]
    return render_template("user/user.html", user=current_user, posts=posts)


@bp.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():

        if db.session.query(User).filter(User.username == form.username.data).first() is not None:
            flash(f"Username '{form.username.data}' is in use by another account, choose another one", category="error")
            return redirect(url_for('user.edit_profile'))

        current_user.username = form.username.data
        current_user.profile.bio = form.bio.data
        db.session.commit()
        flash('Your changes have been saved.', category="success")
        return redirect(url_for('user.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.bio.data = current_user.profile.bio
    return render_template('user/edit_profile.html', title='Edit Profile', form=form)

from app.auth import bp
from flask import render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user

from .. import db
from ..models import User


@bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Login view function
    """
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    # create LoginForm object
    form = LoginForm()

    # validate form on "POST" request
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash("Invalid username/password", category="error")
            return redirect(url_for("auth.login"))

        login_user(user, remember=form.remember.data)

        # redirect to home page
        return redirect(url_for("main.index"))

    # render 'login.html' template with passed form
    return render_template("auth/login.html", form=form)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        # TODO: here create a profile object for this user
        flash("Successfully registered!", category="success")

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

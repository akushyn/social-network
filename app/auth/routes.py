from app.auth import bp
from flask import render_template, redirect, url_for
from .forms import LoginForm


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("index"))
    return render_template("auth/login.html", form=form)
from . import bp
from flask import render_template


@bp.route("/")
@bp.route("/index")
def index():
    context = {
        "user": {"username": "akushyn"},
        "title": "Hillel"
    }
    return render_template("index.html", **context)

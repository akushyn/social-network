from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    context = {
        "user": {"username": "akushyn"},
        "title": "Hillel"
    }
    return render_template("index.html", **context)

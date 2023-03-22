from app import app
from flask import render_template


# register routes
@app.route("/")
@app.route("/index")
def index():
    """
    View function to render home page of the 'Social Network' website
    :return:
    """

    # sample template context to render
    context = {
        "user": {"username": "akushyn"},
        "title": "Hillel"
    }

    # call special function to render template with passed context
    return render_template("index.html", **context)

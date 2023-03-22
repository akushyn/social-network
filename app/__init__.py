from flask import Flask
from config import Config


def create_app():
    """
    Application factory method to create application
    :return: Flask application configured object
    """

    # create instance of Flask object
    app = Flask(__name__)

    # update application config from Config class in config.py
    app.config.from_object(Config)

    # register blueprints here
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app


# create instance of application
app = create_app()

# import routes at the bottom to avoid circular imports
from . import routes

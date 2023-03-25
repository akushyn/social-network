from flask import Flask
from config import Config
from flask_login import current_user


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
    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    @app.context_processor
    def context_processor():
        return dict(
            current_user=current_user
        )
    return app


# create instance of application
app = create_app()


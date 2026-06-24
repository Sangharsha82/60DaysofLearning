from flask import Flask
from .errors import register_error_handlers
from .routes import main_bp


def create_app(config_name="development"):
    app = Flask(__name__)

    # Load config
    from .config import config
    app.config.from_object(config[config_name])

    # Register blueprints
    app.register_blueprint(main_bp)

    # Register error handlers
    register_error_handlers(app)

    return app

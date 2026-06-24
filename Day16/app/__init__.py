from flask import Flask, render_template

from app.api.tasks import tasks_bp


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(tasks_bp)

    @app.get("/")
    def home() -> str:
        return render_template("index.html")

    return app

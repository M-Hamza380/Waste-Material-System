from flask import Flask

from src.waste_management_system.utils.logger import logger

app = Flask(__name__)


def create_app():
    logger.info("Enter into create_app function to create flask app.")

    with app.app_context():
        from src.api.routes.waste_management_system_route import cv

        app.register_blueprint(cv, url_prefix="/")

    logger.info("Exit into create_app function.")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5050, debug=True)

from flask import Blueprint

# from ...waste_management_system.utils.logger import logger

cv = Blueprint("cv", __name__)


@cv.route("/")
def index():
    return "Hello, World!"

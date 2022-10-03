from flask import Flask

application = Flask(__name__)


@application.route("/", methods=["GET"])
def index():
    return "Hello cheta"

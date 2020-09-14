from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from .main import main as newsBlueprint
from .requests import configureRequest

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    app.register_blueprint(newsBlueprint)
    configureRequest(app)

    return app

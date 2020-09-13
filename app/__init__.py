from flask import Flask
from config import config_options
from .main import main as newsBlueprint

def create_app(config_name):
  app = Flask(__name__)
  
  app.config.from_object(config_options[config_name])
  
  app.register_blueprint(newsBlueprint)
  
  return app
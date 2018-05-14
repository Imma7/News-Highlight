from flask import Flask
from flask_bootstrap3 import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint

    #setting config
    from .requests import configure_request #Importing configure_request function
    configure_request(app) #Calling the function and passing the app instance

    # Will add the views and forms

    return app
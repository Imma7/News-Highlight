from flask import Flask
from flask_bootstrap3 import Bootstrap #import bootstrap class from flask_bootstrap extension
from .config import DevConfig #import DevConfig subclass

# Initializing application
app = Flask(__name__)

#Setting up configuration and passing in DevConfig subclass
app.config.from_object(DevConfig)

#Initializing flask extensions
bootstrap.init_app(app) #initializing bootstrap class by passing in the app instance

from app import views

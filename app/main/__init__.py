from flask import Flask
from .config import DevConfig #import DevConfig subclass

# Initializing application
app = Flask(__name__)

#Setting up configuration and passing in DevConfig subclass
app.config.from_object(DevConfig)

from app import views

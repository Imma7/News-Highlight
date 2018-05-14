import urllib.request
import json 
from .models import Article
from .models import Source

#Getting api key
api_key = None
#Getting the news base url
base_url = None

def configure_request(app): #Create a function configure_request
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

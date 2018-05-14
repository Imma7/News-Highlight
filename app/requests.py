import urllib.request
import json 
from .models import Article
from .models import Source

#Getting api key
api_key = None
#Getting the news base url
base_url = None

def configure_request(app):
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

def get_article(self) 
        '''
        Function that gets the json response to our url request
        '''
        get_article_url = base_url.format(category,api_key)

        with urllib.request.urlopen(get_article_url) as url:
            get_article_data = url.read()
            get_movies_response = json.loads(get_article_data.decode(utf-8))

            article_results = None

            if get_article_response['results']:
                article_results_list = get_article_response['articles']
                article_results = process_results(article_results_list)

        return article_results

def get_source(self)
        '''
        Function that gets the json response to our url request 
        '''
        get_movies_url = base_url.format(category,api_key)

        
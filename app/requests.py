import urllib.request
import json 
from .models import Article,Source


#Getting api key
api_key = None
#Getting the news base url
base_url = None

def configure_request(app): #Create a function configure_request
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']

def get_article(id): 
        '''
        Function that gets the json response to our url request
        '''
        get_article_url = base_url.format(id,api_key)

        with urllib.request.urlopen(get_article_url) as url:
            get_article_data = url.read()
            get_article_response = json.loads(get_article_data.decode('utf-8'))

            article_results = None

            if get_article_response['articles']:
                article_results_list = get_article_response['articles']
                article_results = process_articles(article_results_list)

        return article_results

def process_articles(article_list):
        '''
        Function  that processes the article result and transform them to a list of Objects

        Args:
        article_list: A list of dictionaries that contain article details

        Returns :
        article_results: A list of movie objects
        '''
        article_results = []
        for article_item in article_list:
            id = article_item.get('id')
            name = article_item.get('name')
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
            
            if urlToImage:
                article_results = Article(id,name,author,title,description,url,urlToImage,publishedAt)
                article_results.append(article_results)

        return article_results



def get_source(category):
        '''
        Function that gets the json response to our url request 
        '''
        get_source_url = base_url.format(category,api_key)

        with urllib.request.urlopen(get_source_url) as url:
            get_source_data = url.read()
            get_source_response = json.loads(get_source_data.decode('utf-8'))

            source_results = None

            if get_source_response['sources']:
                source_results_list = get_source_response['sources']
                source_results = process_sources(source_results_list)

        return source_results 

def process_sources(source_list):
        '''
        Function  that processes the source result and transform them to a list of Objects

        Args:
        article_list: A list of dictionaries that contain source details

        Returns :
        source_results: A list of movie objects
        '''
        source_results = []
        for source_item in source_list:
            id = source_item.get('id')
            name = source_item.get('name')
            description = source_item.get('description')
            url = source_item('url')
            category = source_item('category')
            language = source_item('language')
            country = source_item('country')

        return source_results

    
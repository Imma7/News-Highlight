import urllib.request
import json 
from .models import Article,Source


#Getting api key
api_key = None
#Getting the news base url
base_url = None

def configure_request(app): #Create a function configure_request
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_ARTICLE_API_BASE_URL']
    base_url = app.config['NEWS_SOURCE_API_BASE_URL']

def get_article(id): #Function that takes in article id as an argument
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

def process_articles(article_list): #Function that takes in a list of dictionaries
        '''
        Function  that processes the article result and transform them to a list of Objects

        Args:
        article_list: A list of dictionaries that contain article details

        Returns :
        article_results: A list of movie objects
        '''
        article_results = [] #Empty list to store newly created article objects
        for article_item in article_list:
            id = article_item.get('id')
            name = article_item.get('name')
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
           #Looping through list of dictionaries using get()method and passing in the keys so that we can access the values
            
            if urlToImage:  #Checking if article item has an image
                article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt) #Creating article object
                article_results.append(article_results) #Appending our empty list

        return article_results #Return list with article objects



def get_source(category): #Function that takes in source category as an argument
        '''
        Function that gets the json response to our url request 
        '''
        get_source_url = base_url.format(category,api_key) #Passing in source category and api key on the base url using the .format method

        with urllib.request.urlopen(get_source_url) as url: #with sends request using urllib.request.urlopen function that takes in get_source_url as an argument and sends a request as url
            get_source_data = url.read() #read function reads the response and stores it in get_source_data variable
            get_source_response = json.loads(get_source_data.decode('utf-8')) #Json response converted to python dictionary passing in get_source_data variable

            source_results = None

            if get_source_response['sources']: #checking if response contains any results
                source_results_list = get_source_response['sources']
                source_results = process_sources(source_results_list) #calling process_sources function and returning list of source objects

        return source_results #return list of source_objects

def process_sources(source_list): #Function that takes in a list of dictionaries
        '''
        Function  that processes the source result and transform them to a list of Objects

        Args:
        article_list: A list of dictionaries that contain source details

        Returns :
        source_results: A list of movie objects
        '''
        source_results = [] #Empty list to store newly created source objects
        for source_item in source_list:
            id = source_item.get('id')
            name = source_item.get('name')
            description = source_item.get('description')
            url = source_item('url')
            category = source_item('category')
            language = source_item('language')
            country = source_item('country')
            #Looping through list of dictionaries using get()method and passing in the keys so that we can access the values

        return source_results

    
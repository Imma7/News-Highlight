import urllib.request
import json 
from .models import Article,Source


#Getting api key
api_key = None
#Getting the news base url
base_article_url = None
base_source_url = None

def configure_request(app): #Create a function configure_request
    global base_article_url,base_source_url
    api_key = app.config['NEWS_API_KEY']
    base_article_url = app.config['NEWS_ARTICLE_API_BASE_URL']
    base_source_url = app.config['NEWS_SOURCE_API_BASE_URL']

def get_article(): #Function that takes in article id as an argument
        '''
        Function that gets the json response to our url request
        '''
        get_article_url = base_article_url.format(api_key)

        with urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f80d5dfbac424cbb9ebffcc23c378ffd") as url:
            get_article_data = url.read()
            get_article_response = json.loads(get_article_data.decode('utf-8'))

            article_results = None
            
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
           
            id = article_item["source"].get("id")  
            name = article_item["source"].get("name") 
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
           #Looping through list of dictionaries using get()method and passing in the keys so that we can access the values
           
            article_object = Article(id,name,author,title,description,url,urlToImage,publishedAt) #Creating article object
            article_results.append(article_object) #Appending our empty list

        return article_results #Return list with article objects



def get_source(): #Function that takes in source category as an argument
        '''
        Function that gets the json response to our url request 
        '''
        get_source_url =  base_source_url.format(api_key) #Passing in source category and api key on the base url using the .format method

        with urllib.request.urlopen('https://newsapi.org/v2/sources?apiKey=f80d5dfbac424cbb9ebffcc23c378ffd') as url: #with sends request using urllib.request.urlopen function that takes in get_source_url as an argument and sends a request as url
            get_source_data = url.read() #read function reads the response and stores it in get_source_data variable
            get_source_response = json.loads(get_source_data.decode('utf-8')) #Json response converted to python dictionary passing in get_source_data variable
        
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
            url = source_item.get('url')
            category = source_item.get('category')
            language = source_item.get('language')
            country = source_item.get('country')
            print(name)

            source = Source(id,name,description,url,category,language,country)
            source_results.append(source)

            #Looping through list of dictionaries using get()method and passing in the keys so that we can access the values

        return source_results

    
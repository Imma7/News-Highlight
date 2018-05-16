import os #Inbuilt method that allows access to the operating system variables like the environment and directories

class Config: #parent Config class contains configurations used in both production and development stages. 

    NEWS_ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={}'
    NEWS_SOURCE_API_BASE_URL ="https://newsapi.org/v2/sources?apiKey={}"

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    #os.environ.get function gets MOVIE_API_KEY and SECRET_KEY which we will set as environment variables

class ProdConfig(Config): #ProdConfig subclass contains configurations used in production stages of our application
    '''
    Production configuration child class 

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config): #DevConfig subclass contains configurations used in development stages of our application
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True #Enables debug mode in our application

#All subclass configs inherit from (Config)parent Class

config_options = {
    'development':DevConfig,
    'production':ProdConfig
} #Dictionary config_options helps us access different configuration option class
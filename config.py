import os

class Config:

    # NEWS_API_BASE_URL = 

    NEWS_API_KEY = os.environ.get('f80d5dfbac424cbb9ebffcc23c378ffd')
    SECRET_KEY = os.environ.get('0719233c9b5e4e3a8337441994ed5d29')
    #os.environ.get function gets MOVIE_API_KEY and SECRET_KEY which we will set as environment variables




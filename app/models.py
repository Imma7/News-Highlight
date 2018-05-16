class Article:
    '''
    Article class to define article objects
    '''

    def __init__(self,id,name,author,title,description,url, urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        
    def __repr__(self):
        return "Article : {}".format(self.name)

    

class Source:
    '''
    Sources class to define sources objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

    def __repr__(self):
        return "Source : {}".format(self.name)
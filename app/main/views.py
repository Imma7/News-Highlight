#Files imports
from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..requests import get_source,get_article
from ..models import Source


#Views
@main.route("/")
def index():
    return render_template("index.html")

@main.route('/articles') #Define route decorator with main blueprint instance
def articles(): #Article function that 
    '''
    View article page function that returns the articles details page and its data
    '''

    articles = get_article()
    return render_template('article.html', articles = articles) #Returns response of article.html

    

@main.route('/sources')
def source():
    '''

    '''
    sources = get_source()
    print(sources)
   
    return render_template('source.html', sources = sources)
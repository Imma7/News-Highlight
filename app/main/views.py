#Files imports
from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..requests import get_source,get_article
from ..models import Source


#Views
@main.route('/article') #Define route decorator with main blueprint instance
def article(id): #Article function that 
    '''
    View article page function that returns the articles details page and its data
    '''

    article = get_article(id)
    
    return render_template('article.html', article = article) #Returns response of article.html

@main.route('/source')
def source(category):
    '''

    '''

    source = get_source(category)

    return render_template('source.html', source = source)
#Files imports
from flask import render_template,request,redirect,url_for
# from app import app
from . import main
from ..requests import get_source,get_article
from ..models import Source


#Views
@main.route('/') #Define route decorator with main blueprint instance
def article(id):
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('article.html') #Returns response of article.html
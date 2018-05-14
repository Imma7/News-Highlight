from flask import render_template
from app import app
from .import main
from .requests import 

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')
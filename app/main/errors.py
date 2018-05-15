from flask import render_template #Importing render template function
# from app import app #Importing flask application instance
from . import main 

@main.errorhandler(404) #Decorator that passes in the error we receive
def four_Ow_four(error): #View function that returns fourOwfour.html file
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404 #Passing in the status code we receive 404



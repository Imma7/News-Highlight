from flask import render_template #Importing render template function
from app import app #Importing flask application instance

@app.errorhandler(404) #Decorator that passes in the error we receive
def four_Ow_four(error): #View function that returns fourOwfour.html file
    '''



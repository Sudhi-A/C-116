#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

#Define a function with differeent endpoints

@app.route("/flask_2")
def second_flask():
    return "python is fun!"

#run the application on local server
app.run(debug=True)

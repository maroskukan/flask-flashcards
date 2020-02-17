from datetime import datetime
from flask import Flask

app = Flask(__name__) # Creates Flask object with name of the module


@app.route("/") # Decorator maps URL to a function defined below
def welcome(): 
    return "Welcome to my Flash Cards application!"

# In backgound, such mapping is added to special attribute app.url_map

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

counter = 0

@app.route("/count_views")
def count_demo():
    global counter
    counter += 1
    return "This page was served " + str(counter) + " times"

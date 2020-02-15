from datetime import datetime
from flask import Flask

# Linux export FLASK_APP=flashcards.py, export FLASK_ENV=development
# Windows set FLASK_APP=flashcards.py, set FLASK_ENV=development
# To run use flask run 

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

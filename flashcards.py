from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"

# Page the counts number of visits

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

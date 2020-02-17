from flask import Flask, render_template

from model import db


app = Flask(__name__) # Creates Flask object with name of the module


@app.route("/") # Decorator maps URL to a function defined below
def welcome():
    return render_template(
        "welcome.html",
        message="Here's a message from the view."
    )


@app.route("/card")
def card_view():
    card = db[0]
    return render_template(
        "card.html",
        card=card
    )

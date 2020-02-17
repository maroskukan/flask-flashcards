from flask import Flask, render_template, abort

from model import db


app = Flask(__name__) # Creates Flask object with name of the module


@app.route("/") # Decorator maps URL to a function defined below
def welcome():
    return render_template(
        "welcome.html",
        message="Here's a message from the view."
    )


@app.route("/card/<int:index>")
def card_view(index):
    try:
        card = db[index]
        return render_template(
            "card.html",
            card=card
        )
    except IndexError:
        abort(404)

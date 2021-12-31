# highLow.py
#
# Python Bootcamp Day 55 - Flask High Low Game
# Usage:
#  Using Flask to generate a website, pick a number between 0-9. Enter your guess
#  as a URL page (eg. http://127.0.0.1:5000/5 or http://127.0.0.1:5000/2)
#
# Marceia Egler December 31, 2021

from flask import Flask
import random

app = Flask(__name__)
num = random.randint(0, 9)


@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Number 7">'


@app.route("/<int:user_pick>")
def guess(user_pick):
    if user_pick == num:
        return (
            "<h1>You found me!</h1>"
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="Correct Guess">'
        )
    elif user_pick < num:
        return (
            "<h1>Too Low!</h1>"
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="Too Low">'
        )
    elif user_pick > num:
        return (
            "<h1>Too High!</h1>"
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="Too High">'
        )


if __name__ == "__main__":
    app.run(debug=True)

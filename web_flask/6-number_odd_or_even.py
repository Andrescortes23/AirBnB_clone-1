#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """To show Hello HBNB"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def home2():
    """To show HBNB"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def homeC(text):
    """Passing variable"""
    return ("C {}".format(text.replace('_', ' ')))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def homePython(text="is cool"):
    """Passing variable with default value"""
    return ("Python {}".format(text.replace('_', ' ')))


@app.route("/number/<int:n>", strict_slashes=False)
def homeInt(n):
    """Passing int varaible"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def homeIntTemplate(n):
    """Display HTML page"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def homeOddorEven(n):
    """Display html and showf odd or even"""
    even = "even"
    odd = "odd"
    if (n % 2 == 0):
        return render_template("6-number_odd_or_even.html", n=n, evenodd=even)
    else:
        return render_template("6-number_odd_or_even.html", n=n, evenodd=odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """To show Hello HBNB"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def home2():
    """To show HBNB"""
    return ("HBNB")


@app.route("/c/<text>='colt'", strict_slashes=False)
def hello_route3(text):
    """Task 2"""
    b = ''
    for a in text:
        if a == '_':
            b += ' '
        else:
            b += a
    return ("C {}".format(b))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)

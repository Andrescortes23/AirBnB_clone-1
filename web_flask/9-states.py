#!/usr/bin/python3
"""
Script that starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def the_states():
    """ HTML the states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, mode="none")


@app.route("/states/<id>", strict_slashes=False)
def the_states_id(id):
    """ HTML the states with id """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state, mode="id")
        else:
            return render_template('9-states.html', states=states, mode="not")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

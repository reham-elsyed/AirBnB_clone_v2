#!/usr/bin/python3
"""
Method to make routes
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """flask"""
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """flask"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """display c and input text"""
    return'c' + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoncool(text='iscool'):
    """python is cool"""
    return 'Python' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')



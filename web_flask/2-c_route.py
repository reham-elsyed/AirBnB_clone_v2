#!/usr/bin/python3
"""
    Module to create routes
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Method hello"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnh():
    """ method hbnb"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """display c and input"""
    return'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

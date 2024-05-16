#/usr/bin/python3
"""Module to use flask to make application"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello world"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb for /hbnb"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

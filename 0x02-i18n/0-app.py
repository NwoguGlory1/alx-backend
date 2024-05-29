#!/usr/bin/env python3
""" Basic Flask app script"""

from flask import Flask, render_template
""" imports necessary module"""

app = Flask(__name__)


@app.route('/')
"""
defines a root in Flask app,
'/' will be accessed when user vivits root URL
"""


def index() -> str:
    """ function that will be called when user visits root URL """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)

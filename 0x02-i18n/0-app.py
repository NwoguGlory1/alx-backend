#!/usr/bin/env python3

""" Module for trying out Babel i18n """

from flask import Flask, render_template
""" imports necessary module"""

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Renders a Basic Template for Babel Implementation"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()

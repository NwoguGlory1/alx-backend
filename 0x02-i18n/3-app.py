#!/usr/bin/env python3
""" Module for trying out Babel i18n """

from flask_babel import Babel, _
from flask import Flask, render_template, request


class Config:
    """ decalring a class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Renders a Basic Template for Babel Implementation"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

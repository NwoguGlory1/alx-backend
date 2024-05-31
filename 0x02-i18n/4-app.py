#!/usr/bin/env python3

""" Module for trying out Babel i18n """

from flask_babel import Babel, _
from flask import Flask, render_template, request
""" imports necessary module"""


class Config:
    """ decalring a class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

SUPPORTED_LOCALES = ['en', 'fr']

@babel.localeselector
def get_locale(request):
    """Determine the best match with our supported languages."""
    locale = request.args.get('locale')
    if locale in SUPPORTED_LOCALES:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Renders a Basic Template for Babel Implementation"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)

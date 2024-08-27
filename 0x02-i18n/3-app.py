#!/usr/bin/env python3
"""Basic Babel setup."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration of available languages in our app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine best match with supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """Basic app for index.html template."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()

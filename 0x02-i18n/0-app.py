#!/usr/bin/env python3
"""Basic Flask app setup."""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello():
    """Basic app for index.html template."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()

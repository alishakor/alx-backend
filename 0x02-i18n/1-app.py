#!/usr/bin/env python3
"""Flask app and babel class"""
from flask_babel import Babel
from flask import Flask, render_template

# create the flask Instance
app = Flask(__name__)


class Config:
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


# create route decorator
@app.route('/', strict_slashes=False)
def index() -> str:
    """returns the 0-index.html page"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

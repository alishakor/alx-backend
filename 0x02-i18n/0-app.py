#!/usr/bin/env python3
"""Flask app Setup"""

from flask import Flask, render_template

# create the flask Instance
app = Flask(__name__)


# create route decorator
@app.route('/', strict_slashes=False)
def index() -> str:
    """returns the 0-index.html page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# =============================================================================
# Pokemon Shiny Tracker
# Author: Joshua Jewson
# Email:  joshuajewson@icloud.com
# =============================================================================

"""
app.py

Entry point for the Pokemon Shiny Tracker Flask application.
Creates the Flask app instance, registers routes, and starts the
development server when run directly.
"""

from flask import Flask, render_template, request

# Create the Flask application instance
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form.get("pokemon-name"))
    return render_template("index.html")


if __name__ == "__main__":
    # Run with debug=True to enable hot-reload during development
    app.run(debug=True)

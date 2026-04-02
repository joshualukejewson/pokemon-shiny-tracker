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

from flask import Flask, render_template, request, url_for
from services.pokeapi import get_individual_pokemon_data
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "bulbasauristhebestgen1starter"
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/hunt", methods=["GET", "POST"])
def hunt():
    """Render the shiny hunt page.

    GET:  Renders the empty hunt template.
    POST: Reads the 'pokemon-name' form field, fetches the Pokemon's data
          from the PokeAPI, and re-renders the template with the result.
          If the name is missing or not found, falls back to the empty template.
    """
    if request.method == "POST":
        pokemon_name = request.form.get("pokemon-name")
        pokemon_data = None
        if pokemon_name:
            pokemon_data = get_individual_pokemon_data(pokemon_name)
        if pokemon_data:
            return render_template("hunt.html", pokemon=pokemon_data)

    return render_template("hunt.html")


if __name__ == "__main__":
    app.run(debug=True)

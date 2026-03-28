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
from services.pokeapi import get_individual_pokemon_data
from modules.pokemon import Pokemon

# Create the Flask application instance
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the home page.

    GET:  Renders the empty index template.
    POST: Reads the 'pokemon-name' form field, fetches the Pokemon's data
          from the PokeAPI, and re-renders the template with the result.
          If the name is missing or not found, falls back to the empty template.
    """
    if request.method == "POST":
        pokemon_name = request.form.get("pokemon-name")
        pokemon = None
        if pokemon_name:
            pokemon = get_individual_pokemon_data(pokemon_name)
            if pokemon:
                print(pokemon.name)
                return render_template("index.html", pokemon=pokemon)

    return render_template("index.html")


if __name__ == "__main__":
    # Run with debug=True to enable hot-reload during development
    app.run(debug=True)

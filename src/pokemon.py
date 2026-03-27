"""
pokemon.py

Utilities for fetching Pokemon data from the PokeAPI (https://pokeapi.co).
"""

import requests

POKEAPI_BASE = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_data(name: str) -> dict:
    """
    Fetch data for a Pokemon by name from the PokeAPI.

    Args:
        name: The Pokemon's name (e.g. "ditto", "pikachu").

    Returns:
        A dict containing the Pokemon's data on success, or an empty dict
        if the request fails.
    """
    response = requests.get(f"{POKEAPI_BASE}{name}")
    if response.status_code == 200:
        print(response.text)
    return {}


get_pokemon_data("ditto")

from modules.pokemon import Pokemon
import requests

POKEAPI_BASE = "https://pokeapi.co/api/v2/pokemon/"


def get_individual_pokemon_data(name: str) -> Pokemon | None:
    """Fetch a single Pokemon's data from the PokeAPI and return a Pokemon object.

    Makes a GET request to the PokeAPI using the provided name. Extracts the
    Pokemon's ID and animated showdown sprites (normal and shiny).

    Args:
        name: The Pokemon's name (case-insensitive).

    Returns:
        A Pokemon instance if the request succeeds, or None if the Pokemon
        is not found (non-200 response).
    """

    response = requests.get(f"{POKEAPI_BASE}{name.lower()}")
    if response.status_code != 200:
        return None
    data = response.json()
    # Pokemon object build
    poke_name = name.lower()
    poke_id = data["id"]
    nsprite = data["sprites"]["other"]["showdown"]["front_default"]
    ssprite = data["sprites"]["other"]["showdown"]["front_shiny"]
    return Pokemon(poke_id, poke_name, nsprite, ssprite)

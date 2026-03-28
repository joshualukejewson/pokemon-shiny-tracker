from modules.pokemon import Pokemon
import requests

POKEAPI_BASE = "https://pokeapi.co/api/v2/pokemon/"


def get_individual_pokemon_data(name: str) -> Pokemon | None:
    response = requests.get(f"{POKEAPI_BASE}{name.lower()}")
    if response.status_code != 200:
        return None
    data = response.json()
    pokemon_name = name.lower()
    id = data["id"]
    nsprite = data["sprites"]["other"]["showdown"]["front_default"]
    ssprite = data["sprites"]["other"]["showdown"]["front_shiny"]
    print(data)
    return Pokemon(id, pokemon_name, nsprite, ssprite)

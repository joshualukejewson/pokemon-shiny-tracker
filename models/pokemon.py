from dataclasses import dataclass
from typing import Optional


@dataclass
class Pokemon:
    """Represents a Pokemon with its display sprites and caught status."""

    """
    Args:
        id: The PokeAPI numeric ID for the Pokemon.
        name: Lowercase name of the Pokemon (e.g. "pikachu").
        normal_sprite: URL to the normal animated front sprite.
        shiny_sprite: URL to the shiny animated front sprite.
        caught: Whether the shiny has been caught. Defaults to False.
    """
    id: int
    name: str
    normal_sprite: str
    shiny_sprite: str
    caught: Optional[bool] = None

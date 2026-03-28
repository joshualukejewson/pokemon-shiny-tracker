class Pokemon:
    """Represents a Pokemon with its display sprites and caught status."""

    def __init__(self, id, name, normal_sprite, shiny_sprite, caught=False) -> None:
        """
        Args:
            id: The PokeAPI numeric ID for the Pokemon.
            name: Lowercase name of the Pokemon (e.g. "pikachu").
            normal_sprite: URL to the normal animated front sprite.
            shiny_sprite: URL to the shiny animated front sprite.
            caught: Whether the shiny has been caught. Defaults to False.
        """
        self.id = (id,)
        self.name = name
        self.normal_sprite = normal_sprite
        self.shiny_sprite = shiny_sprite
        self.caught = caught

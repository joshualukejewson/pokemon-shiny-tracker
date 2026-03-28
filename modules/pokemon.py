class Pokemon:
    def __init__(self, id, name, normal_sprite, shiny_sprite, caught=False) -> None:
        self.id = (id,)
        self.name = name
        self.normal_sprite = normal_sprite
        self.shiny_sprite = shiny_sprite
        self.caught = caught

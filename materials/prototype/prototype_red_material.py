from ursina import *


class PrototypeRedMaterial(Entity):
    def __init__(self, variation=1, **kwargs):
        super().__init__(**kwargs)
        self.texture = f"textures/prototype/red/texture_{str(variation).zfill(2)}.png"

        for key, value in kwargs.items():
            setattr(self, key, value)

from abstracts import Material


class PrototypeGreenMaterial(Material):
    def __init__(self, variation=1, **kwargs):
        super().__init__(**kwargs)
        self.texture = f"textures/prototype/green/texture_{str(variation).zfill(2)}.png"

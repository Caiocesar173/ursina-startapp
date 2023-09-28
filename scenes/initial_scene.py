from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from materials.prototype.prototype_dark_material import PrototypeDarkMaterial
from materials.prototype.prototype_light_material import PrototypeLightMaterial

class InitialScene(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'initial_scene'

        # Carregar o shader básico
        self.shader = Shader(language=Shader.GLSL, path='shaders/basic_shader.glsl')

        # Configurações da câmera
        self.camera = FirstPersonController()

        # Configurações de luz
        self.light = DirectionalLight(parent=self)
        self.light.position = (2, 4, 1)

        # Entidades
        self.floor = Entity(model='plane', scale=(10, 1, 10), material=PrototypeDarkMaterial(), color=color.azure, collider='box')
        self.cube = Entity(model='cube', position=(0, 1, 0), material=PrototypeLightMaterial())

        # Lógica de inicialização
        self.initialize()

    def initialize(self):
        print("Cena inicial carregada com sucesso!")

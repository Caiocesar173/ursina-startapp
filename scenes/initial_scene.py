from ursina import Shader, DirectionalLight
from ursina.prefabs.first_person_controller import FirstPersonController

from abstracts import GameObject
from materials.prototype import PrototypeDarkMaterial, PrototypeLightMaterial


class InitialScene(GameObject):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'initial_scene'

        # Carregar o shader básico
        # self.shader = Shader(language=Shader.GLSL, path='shaders/basic_shader.glsl')

        # Configurações da câmera
        self.camera = FirstPersonController()

        # Configurações de luz
        self.light = DirectionalLight(parent=self)
        self.light.position = (2, 4, 1)

        # Entidades
        self.floor = GameObject(model='plane', scale=(100, 1, 100), material=PrototypeDarkMaterial(), collider='box')
        self.cube = GameObject(model='cube', position=(0, 1, 0), material=PrototypeLightMaterial(), collider='box')

        # Lógica de inicialização
        self.initialize()

    def initialize(self):
        print("Cena inicial carregada com sucesso!")

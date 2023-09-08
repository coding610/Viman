from Viman.scene.surface import *


class Scene:
    def __init__(self) -> None:
        self.objects = {}
        self.surfaces = {}

    def build(self): pass
    def update(self): pass

    def new_surface(self, id: str, surface: Surface):
        self.surfaces[id] = surface

        return self.surfaces

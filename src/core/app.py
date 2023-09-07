import pygame
from core import artist
from core import scene
from log import log


class App:
    def __init__(self, resolution: tuple) -> None:
        self.resolution = resolution
        self._window = pygame.display.set_mode(resolution)

        self.artist = artist.Artist(self._window) # Drawer
        self.scenes = {}

        self.logger = log.Logger()

    def new_scene(self, name: str, set_scene: bool=True) -> scene.Scene:
        self.scenes[name] = scene.Scene()
        if set_scene: self.scene = self.scenes[name]

        return self.scene

    def run(self):
        self.running = True
        while self.running:
            self.scene.handle_events()
            self.artist.draw(self.scene.objects)

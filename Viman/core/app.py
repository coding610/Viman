import pygame
from Viman.core.artist import *
from Viman.scene.scene import *
from Viman.log.log import *


class App:
    def __init__(self, resolution: tuple, fps: float=60) -> None:
        self.resolution = resolution
        self.fps = fps

        self.__window = pygame.display.set_mode(resolution)
        self.scenes = {}
        self.scene: Scene

        self.artist = Artist(self.__window) # Drawer
        self.logger = Logger()

    def run(self):
        self.running = True
        while self.running:
            self.__handle_events()
            self.scene.update()

            self.__window = self.artist.draw(self.scene.surface)

    # -1 is on top
    # 0 is on bottom
    # 1 is above 0
    def attatch_scene(self, scene: Scene, target: bool=True):
        name = scene.__class__.__name__
        self.scenes[name] = scene
        if target: self.scene = self.scenes[name]


    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

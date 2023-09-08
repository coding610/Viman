import pygame
from Viman.scene.surface import *
from Viman.scene.group import *


class Artist:
    def __init__(self, window) -> None:
        self.__window: pygame.surface.Surface = window

    def draw(self, surface: Surface) -> pygame.surface.Surface:
        print(type(self.__window))
        if type(surface) == RelativeSurface:
            # Objects get drawn in no particular order
            # Fix this in the future
            self.__draw_objects(surface.objects)
            for g in surface.groups: self.__draw_objects(g.objects)

            print(surface.groups["nodes"].objects[3].objects["a"].text)


        return self.__window


    def __draw_objects(self, objects):
        for o in objects:
            self.__window = o.draw(self.__window) # AHHH GET ME POINTERS PYTHON!!!
            # Ouuuh recursive olala
            if type(o) == Group: self.__draw_objects(o.objects)

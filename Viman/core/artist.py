import pygame
import itertools
from Viman.scene.surface import *
from Viman.scene.group import *


class Artist:
    def __init__(self, window) -> None:
        self.__window: pygame.surface.Surface = window
        self.increment = 0

    def draw(self, surface: Surface) -> pygame.surface.Surface:
        if type(surface) == RelativeSurface:
            # Objects get drawn in no particular order
            # Fix this in the future
            self.__draw_objects(surface.objects)
            for g in surface.groups:
                g = surface.groups[g]
                self.__draw_objects(g.objects)

        return self.__window


    def __draw_objects(self, objects):
        # Collapse objects and groups into one list
        c_objects = self.__collapse_group(objects)

        for o in c_objects:
            self.increment += 1

            self.__window = o.draw(self.__window, self.increment)

    def __collapse_group(self, group_objects) -> list:
        c_objects = []
        for o in group_objects:
            o = group_objects[o]
            if type(o) == Group:
                for g in self.__collapse_group(o.objects):
                    c_objects.append(g)
            else:
                c_objects.append(o)

        return c_objects

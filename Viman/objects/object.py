import pygame


# Thin wrapper around other shapes
class Object:
    def __init__(self) -> None:
        pass

    def draw(self, window: pygame.surface.Surface) -> pygame.surface.Surface:
        return window

import pygame


# Thin wrapper around other shapes
class Object:
    def __init__(self) -> None:
        self.absolute_position = (0, 0)

    def draw(self, window: pygame.surface.Surface) -> pygame.surface.Surface:
        return window

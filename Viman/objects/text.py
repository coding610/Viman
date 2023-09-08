import pygame
from Viman.scene.group import *
from Viman.objects.object import Object
from Viman.core.font import Font


class Text(Object):
    def __init__(
        self,
        text: str,
        color: tuple=(255, 255, 255),
        font: Font=Font("Arial", 30),
        position: RelativePosition | GridPosition | AbsolutePosition | None=None,
    ) -> None:
        super().__init__()
        self.text = text
        self.font = font
        self.position = position
        self.color = color

    def draw(self, window: pygame.surface.Surface, increment) -> pygame.surface.Surface:
        w, h = window.get_width(), window.get_height()
        
        # FIXME
        self.font.font.render_to(window, (50 * increment, 50 * increment), self.text, self.color)

        return window

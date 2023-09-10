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

        self.currentrender = self.font.font.render(text)[0]
        self.dims = (self.currentrender.get_width(), self.currentrender.get_height())

    def draw(self, window: pygame.surface.Surface) -> pygame.surface.Surface:
        self.font.font.render_to(window, (self.absolute_position), self.text, self.color)

        return window

    def update_text(self, text):
        print("NEED TO UPDATE CURRENTRENDER AND DIMS WHEN DOING THIS")

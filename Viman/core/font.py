import pygame.freetype


class Font:
    def __init__(self, font: str, size: int, path: str | None=None) -> None:
        if path == None:
            self.font = pygame.freetype.SysFont(font, size)
        else:
            self.font = pygame.freetype.Font(path, size)

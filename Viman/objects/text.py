from Viman.scene.group import *
from Viman.objects.object import Object


class Text(Object):
    def __init__(self, text, position: RelativePosition | GridPosition | AbsolutePosition | None=None) -> None:
        self.text = text
        self.position = position # Middle if relative and grid. Top left if Absolute
                                 # Artists job to decide

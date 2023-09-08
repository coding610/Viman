from Viman.scene.group import *
from Viman.objects.text import Text
from Viman.objects.object import Object


class Surface:
    def __init__(self) -> None:
        self.objects = {}

    # Shurtcut for new_object
    def new_text(
        self,
        id: str,
        text: str,
        position: RelativePosition | GridPosition | AbsolutePosition = RelativePosition.Center
    ): self.objects[id] = Text(text, position=position) # Its the artist job to handle where to place them

    # Create object in paramter
    def new_object(
        self,
        id: str,
        object: Object,
    ): self.objects[id] = object

class RelativeSurface(Surface):
    def __init__(self) -> None:
        super().__init__()
        self.groups = {}

    def append_group(self, id: str, group: Group):
        self.groups[id] = group
        for o in self.groups[id].objects:
            o = self.groups[id].objects[o]
            o.position = self.groups[id].position

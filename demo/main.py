from copy import copy

from Viman.core.init import init
init()

from Viman.core.app import App
from Viman.objects.text import Text
from Viman.scene.group import *
from Viman.scene.surface import *
from Viman.scene.scene import *


class HomeScene(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.surface = RelativeSurface(spacing=100)

        self.surface.new_text(id="maintext", text="Alone object", position=RelativePosition.Center)

        self.nodes = Group(RelativePosition.TopRight, GroupAligment.Horizontal, 300)
        self.nodes.append_objects((
                [Text("Nodes"), "a"],
            ),
            automatic_ids=False
        )

        self.othernodes = Group(RelativePosition.Center, GroupAligment.Horizontal, 300)
        self.othernodes.append_objects(
            (
                Text("Othernodes"), # id 0
                self.nodes
            ),
        )

        self.surface.append_group(id="nodes", group=self.nodes)
        self.surface.append_group(id="othernodes", group=self.othernodes)

        self.surface = super().new_surface("relative", self.surface)


App = App((1440, 810), fps=60)
App.attatch_scene(HomeScene(), target=True)

App.run()

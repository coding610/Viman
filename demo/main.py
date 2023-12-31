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
        self.surface = RelativeSurface(spacing=10)

        self.surface.new_text(id="maintext", text="Hi JOOHN", position=RelativePosition.Center)

        self.nodes = Group(RelativePosition.BottomLeft, GroupAligment.Horizontal, 10)
        self.nodes.append_objects((
                [Text("Hello World"), "a"],
                [Text("You Know it"), "b"],
                [Text("Yheaaaaaaaa"), "c"],
            ),
            automatic_ids=False
        )

        self.othernodes = Group(RelativePosition.Center, GroupAligment.Horizontal, 10)
        self.othernodes.append_objects(
            (
                Text("This is automatic"), # id 0
                Text("Feels soo good"), # id 1
                Text("Wooohoo"), # id 2
                copy(self.nodes) # id 3
            ),
        )

        self.surface.append_group(id="nodes", group=self.nodes)
        self.surface.append_group(id="othernodes", group=self.othernodes)

        self.surface = super().new_surface("relative", self.surface)


App = App((1440, 810), fps=60)
App.attatch_scene(HomeScene(), target=True)

App.run()

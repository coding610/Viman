from shapes.shape import Shape

class Scene:
    def __init__(self) -> None:
        self.objects = {}

    def new_object(self, name: str, shape: Shape, is_interactive: bool=True):
        self.objects[name] = {"is_interactive": is_interactive, "shape": Shape}

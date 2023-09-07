from shapes.shape import Shape


class Rectangle(Shape):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

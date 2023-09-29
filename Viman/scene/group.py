import enum


class GroupAligment(enum.Enum):
    Horizontal = 1
    Vertical = 2

############################ POSITIONS ########################
class RelativePosition(enum.Enum):
    Center = 1
    TopLeft = 2
    TopRight = 3
    BottomLeft = 4
    BottomRight = 5

class GridPosition:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column


class AbsolutePosition:
    def __init__(self, x, y) -> None:
        self.position = (x, y)
############################ POSITIONS ########################

class Group:
    def __init__(
        self,
        position: RelativePosition | GridPosition | AbsolutePosition, # Remember: only can have gridpos if grid surface and vice versa
        order: GroupAligment=GroupAligment.Horizontal,
        spacing: int=10
    ) -> None:
        self.objects = {}
        self.aligment = order
        self.spacing = spacing
        self.position = position

    def append_objects(self, objects: tuple | list[tuple], automatic_ids: bool=True, natural_order: bool=True):
        # Can either be Object or Group
        # Artist should handle it

        # Auto ids will be ints to differentiate between chosen ids
        if natural_order:
            for o, id in zip(objects, range(0, len(objects))):
                if automatic_ids:
                    self.objects[id] = self.__group_to_dict(o)
                else:
                    self.objects[o[1]] = self.__group_to_dict(o[0])
        else:
            for o, id in zip(reversed(objects), reversed(range(0, len(objects)))):
                if automatic_ids:
                    self.objects[id] = self.__group_to_dict(o)
                else:
                    self.objects[o[1]] = self.__group_to_dict(o[0])

    def __group_to_dict(self, og): # Og is either object or Group
        if type(og) == Group:
            for o in og.objects:
                og.objects[o] = self.__group_to_dict(og.objects)

        return og

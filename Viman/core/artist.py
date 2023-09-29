from copy import copy
import pygame
from Viman.scene.surface import *
from Viman.scene.group import *


class Artist:
    def __init__(self, window) -> None:
        self.__window: pygame.surface.Surface = window
        self.increment = 0

    def draw(self, surface: Surface) -> pygame.surface.Surface:
        if type(surface) == RelativeSurface:
            # Objects get drawn in no particular order
            # Fix this in the future
            self.__draw_objects(surface.objects, surface.spacing)
            for g in surface.groups:
                g = surface.groups[g]
                print(f"OUTSIDE OBJECTS IN GROUPS: {g.objects}")
                self.__draw_objects(g, surface.spacing)

        return self.__window

    def __draw_objects(self, g: Group | dict, spacing: int):
        group = copy(g)

        if type(group) == Group: objects: dict = group.objects
        elif type(group) == dict: objects: dict = group
        else: objects: dict = {}

        if type(group) == Group:
            positions = self.__position_groups(group, spacing)
            objects = self.__handle_postitions(group, positions).objects

        elif type(group) == dict:
            objects = self.__position_objects(objects, spacing)

        objects = self.__adjust_positions(objects)
        listed_objects: list = self.__collapse_group(objects)

        print(f"LISTED OBJECTS: {listed_objects}")
        print(f"OBJECTS: {objects}")
        for o in listed_objects:
            self.__window = o.draw(self.__window)

    def __collapse_group(self, group_objects: dict) -> list:
        c_objects = []
        for o in group_objects:
            o = group_objects[o]
            if type(o) == Group:
                for g in self.__collapse_group(o.objects):
                    c_objects.append(g)
            else:
                c_objects.append(o)

        return c_objects


    def __position_objects(self, objects: dict, spacing) -> dict:
        w, h = self.__window.get_width(), self.__window.get_height()
        
        for o in objects:
            if type(objects[o].position) == Group:
                objects = self.__position_objects(o.objects, spacing)

            if type(objects[o].position) == RelativePosition:
                if objects[o].position == RelativePosition.Center:
                    objects[o].absolute_position = (w/2, h/2)
                elif objects[o].position == RelativePosition.TopLeft:
                    objects[o].absolute_position = (spacing, spacing)
                elif objects[o].position == RelativePosition.TopRight:
                    objects[o].absolute_position = (spacing, w - spacing)
                elif objects[o].position == RelativePosition.BottomLeft:
                    objects[o].absolute_position = (h - spacing, spacing)
                elif objects[o].position == RelativePosition.BottomRight:
                    objects[o].absolute_position = (h - spacing, w - spacing)

        return objects
        
    # This will only be on relative surfaces
    def __position_groups(self, group: Group, spacing) -> list:
        w, h = self.__window.get_width(), self.__window.get_height()

        objects = group.objects

        positions: list = [(), []]
        current_position = (-spacing, -spacing)
        for o in objects:
            if type(objects[o]) == Group:
                positions[1].append([(0, 0), self.__position_groups(objects[o], spacing)[1]])
            else:
                if group.aligment == GroupAligment.Horizontal:
                    positions[1].append(( current_position[0] + group.spacing, 0 ))
                    current_position = ( current_position[0] + group.spacing, 0 )
                else:
                    positions[1].append(( 0, current_position[1] + group.spacing ))
                    current_position = ( 0, current_position[1] + group.spacing )

        group_position = objects[next(iter(objects))].position
        if group_position == RelativePosition.Center:
            positions[0] = (w/2, h/2)
        elif group_position == RelativePosition.TopLeft:
            positions[0] = (spacing, spacing)
        elif group_position == RelativePosition.TopRight:
            positions[0] = (spacing, w - spacing)
        elif group_position == RelativePosition.BottomLeft:
            positions[0] = (h - spacing, spacing)
        elif group_position == RelativePosition.BottomRight:
            positions[0] = (h - spacing, w - spacing)

        return positions

    def __handle_postitions(self, group: Group, positions: list) -> Group:
        objects = group.objects
        for o, p in zip(objects, range(len(positions[1]))):
            if type(objects[o]) == Group:
                objects[o] = self.__handle_postitions(objects[o], positions[1][p])
            else:
                print(p, o, type(objects[o]), objects, positions)
                objects[o].absolute_position = (
                    positions[1][p][0] + positions[0][0],
                    positions[1][p][1] + positions[0][1]
                )

        group.objects = objects
        return group

    def __adjust_positions(self, objects: dict) -> dict:
        return objects

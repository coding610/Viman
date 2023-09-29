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
                self.__draw_objects(surface.groups[g], surface.spacing)

        return self.__window

    def __draw_objects(self, group: dict | Group, surface_spacing: int):
        if type(group) == Group:
            objects: dict = group.objects
            positions = self.__position_groups(group, objects, surface_spacing)
            objects = self.__handle_postitions(objects, positions) # This both collapses and treats objects
            objects = self.__adjust_positions(objects)
        elif type(group) == dict:
            objects: dict = group
            objects = self.__position_objects(objects, surface_spacing)
        else:
            objects = {}

        listed_objects: list = self.__list_group(objects)
        for o in listed_objects:
            self.__window = o.draw(self.__window)

    def __list_group(self, group_objects: dict) -> list:
        c_objects = []
        for o in group_objects:
            o = group_objects[o]
            if type(o) == dict:
                for g in self.__list_group(o):
                    c_objects.append(g)
            else:
                c_objects.append(o)

        return c_objects


    def __position_objects(self, objects: dict, surface_spacing) -> dict:
        w, h = self.__window.get_width(), self.__window.get_height()
        
        for o in objects:
            if type(objects[o].position) == dict:
                objects = self.__position_objects(o.objects, surface_spacing)

            if type(objects[o].position) == RelativePosition:
                if objects[o].position == RelativePosition.Center:
                    objects[o].absolute_position = (w/2, h/2)
                elif objects[o].position == RelativePosition.TopLeft:
                    objects[o].absolute_position = (surface_spacing, surface_spacing)
                elif objects[o].position == RelativePosition.TopRight:
                    objects[o].absolute_position = (surface_spacing, w - surface_spacing)
                elif objects[o].position == RelativePosition.BottomLeft:
                    objects[o].absolute_position = (h - surface_spacing, surface_spacing)
                elif objects[o].position == RelativePosition.BottomRight:
                    objects[o].absolute_position = (h - surface_spacing, w - surface_spacing)

        return objects
        
    # This will only be on relative surfaces
    # Group parameter is only for top group params
    def __position_groups(self, group: Group, objects: dict, surface_spacing) -> list:
        w, h = self.__window.get_width(), self.__window.get_height()

        positions: list = [(), []]
        current_position = (-surface_spacing, -surface_spacing)
        for o in objects:
            if type(objects[o]) == dict:
                positions[1].append([(0, 0), self.__position_groups(group, objects[o], surface_spacing)[1]])
            else:
                if group.aligment == GroupAligment.Horizontal:
                    current_position = ( current_position[0] + group.spacing, 0 )
                    positions[1].append(current_position)
                else:
                    current_position = ( 0, current_position[1] + group.spacing )
                    positions[1].append(current_position)

        group_position = objects[next(iter(objects))].position
        if group_position == RelativePosition.Center:
            positions[0] = (w/2, h/2)
        elif group_position == RelativePosition.TopLeft:
            positions[0] = (surface_spacing, surface_spacing)
        elif group_position == RelativePosition.TopRight:
            positions[0] = (surface_spacing, w - surface_spacing)
        elif group_position == RelativePosition.BottomLeft:
            positions[0] = (h - surface_spacing, surface_spacing)
        elif group_position == RelativePosition.BottomRight:
            positions[0] = (h - surface_spacing, w - surface_spacing)

        return positions

    def __handle_postitions(self, objects: dict, positions: list) -> dict:
        for o, p in zip(objects, range(len(positions[1]))):
            if type(objects[o]) == dict:
                objects[o] = self.__handle_postitions(objects[o], positions[1][p])
            else:
                objects[o].absolute_position = (
                    positions[1][p][0] + positions[0][0],
                    positions[1][p][1] + positions[0][1]
                )

        return objects

    def __adjust_positions(self, objects: dict) -> dict:
        return objects

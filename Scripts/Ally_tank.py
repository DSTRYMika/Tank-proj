import math
from typing import Optional, Tuple

import pygame
from pygame import Surface

from Draw import Drawable
from Scripts.FixedStrings import KEY_POS_X, KEY_POS_Y, KEY_ROT, DRAWING_ROT

WIDTH, HEIGHT = 600, 400


class Ally_tank(Drawable):

    def get_rotation(self):
        return self.properties[KEY_ROT]

    def set_rotation(self, angle):
        self.properties[KEY_ROT]= angle

    def __init__(self):
        Drawable.__init__(self)
        self.velocity_x: float = 0.0
        self.velocity_y: float = 0.0
        self.friction = 0.92
        self.tank = pygame.image.load("../Sprites/ally.png")
        self.tank_width, self.tank_height = self.tank.get_size()
        self.rect = pygame.Rect(0, 0, self.tank_width, self.tank_height)
        max_edge=max(self.tank_width, self.tank_height)
        self.square_size = max_edge
        self.square_surf = pygame.Surface((self.square_size, self.square_size), pygame.SRCALPHA)
        #self.square_rect = self.square_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.frame_until_trail = 10
        self.cached_drawings = []

    def get_trail_emitter(self) -> tuple[int, str] | None:
        pos_x = self.properties[KEY_POS_X]
        pos_y = self.properties[KEY_POS_Y]
        rotation_rad = self.get_rotation() / 180 * math.pi
        accel_x = -math.sin(rotation_rad) * self.tank_width /2
        accel_y = -math.cos(rotation_rad) * self.tank_height /2
        return pos_x+accel_x,pos_y+accel_y

    def get_drawing_rotation(self) -> int:
        return int(self.get_rotation()/15)


    def add_to_cached_list(self, rotation : int, surface: Surface):
        new_drawing = [rotation, surface]
        self.cached_drawings.append(new_drawing)

    def is_drawing_rotation_cached(self, rotation):
        for i in self.cached_drawings:
            if i[0] == rotation:
                return i
        return None

    def draw(self, screen: Surface):
        print(self.properties[DRAWING_ROT])
        print(self.properties[KEY_ROT])
        pos_x = self.properties[KEY_POS_X]
        pos_y = self.properties[KEY_POS_Y]
        # tank
        self.square_surf.blit(self.tank, (self.square_size/2-self.tank_width / 2, self.square_size/2-self.tank_height / 2))

        cached_func_result = self.is_drawing_rotation_cached(self.properties[DRAWING_ROT])

        if cached_func_result is not None:
            rotated_surf = cached_func_result[1]
            size_rotated = rotated_surf.get_size()
            screen.blit(rotated_surf, (pos_x - size_rotated[0] / 2, pos_y - size_rotated[1] / 2))

        else :
            # Faire tourner la surface contenant le carré
            rotated_surf = pygame.transform.rotate(self.square_surf, self.get_drawing_rotation())
            size_rotated = rotated_surf.get_size()

            #Caching de la surface
            self.add_to_cached_list(self.properties[DRAWING_ROT], rotated_surf)

            # Afficher la surface tournée sur l’écran principal

            screen.blit(rotated_surf, (pos_x - size_rotated[0] / 2, pos_y - size_rotated[1] / 2))

    def move(self, distance: float):
        # Compute acceleration vector (direction based on tank rotation)
        rotation_rad = self.get_rotation() / 180 * math.pi
        accel_x = math.sin(rotation_rad) * distance
        accel_y = math.cos(rotation_rad) * distance

        # Apply acceleration to velocity
        self.velocity_x += accel_x
        self.velocity_y += accel_y

    def update_position(self, delta_time: float):
        self.properties[KEY_POS_X] += self.velocity_x * delta_time * 10
        self.properties[KEY_POS_Y] += self.velocity_y * delta_time * 10

        self.velocity_x *= self.friction
        self.velocity_y *= self.friction


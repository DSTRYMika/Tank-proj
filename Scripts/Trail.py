from xmlrpc.client import FastParser

import pygame
from pygame import Surface

from Scripts.Ally_tank import Ally_tank
from Scripts.Draw import Drawable
from Scripts.FixedStrings import KEY_POS_X, KEY_POS_Y


class Trail(Drawable):

    def __init__(self, generator: Drawable):
        Drawable.__init__(self)
        self.DEBUG: bool=False
        self.generator: Drawable = generator
        self.trail = pygame.image.load("../Sprites/smoke.png")
        self.trail_width, self.trail_height = self.trail.get_size()
        self.square_surf = pygame.Surface((self.trail_width, self.trail_height), pygame.SRCALPHA)
        self.frame_left = 10
        self.trail_list = []
        if not generator.get_trail_emitter():
            raise Exception("Added trail to a Drawable that has no trail emitter")

        self.max_density = 128
        self.trail_density = self.max_density / self.frame_left

    def draw(self, screen: Surface):
        #pos_x = self.generator.properties[KEY_POS_X]
        #pos_y = self.generator.properties[KEY_POS_Y]
        pos_x, pos_y = self.generator.get_trail_emitter()

        if self.frame_left == 0:
            self.frame_left = 10
            if self.DEBUG:
                print(f"DEBUG TRAIL # append {pos_x},{pos_y} ")
            self.trail_list.append([pos_x, pos_y])
            if len(self.trail_list) >= 11:
                self.trail_list.pop(0)
        else:
            self.frame_left -= 1
        iteration = 1

        for i in self.trail_list:
            density = min(255,max(0,iteration * self.trail_density))
            trail_copy = self.trail.copy()
            trail_copy.fill((255, 255, 255, density), special_flags=pygame.BLEND_RGBA_MULT)

            if self.DEBUG:
                print(f"DEBUG TRAIL # draw {i[0]},{i[1]}  density={density}")
            screen.blit(trail_copy, (i[0] - self.trail_width / 2 ,i[1] - self.trail_height / 2 ))
            iteration += 1


        # Faire tourner la surface contenant le carré
        # rotated_surf = pygame.transform.rotate(self.square_surf, self.get_rotation())

    # rotated_rect = rotated_surf.get_rect(center=(pos_x, pos_y))

    # Afficher la surface tournée sur l’écran principal
    #  rotated_rect = rotated_rect.move(self.trail_width, self.trail_height)

    # screen.blit(rotated_surf, rotated_rect)

    def update_position(self, delta_time: float):
        pass

    def move(self, distance: float):
        pass

    def set_rotation(self, angle):
        pass

    def get_rotation(self):
        pass
import pygame
from pygame import Surface

from Scripts.Draw import Drawable
from Scripts.FixedStrings import KEY_POS_X, KEY_POS_Y


class Trail(Drawable):

    def __init__(self, generator: Drawable):
        Drawable.__init__(self)
        self.generator= generator
        self.trail = pygame.image.load("../Sprites/smoke.png")
        self.trail_width,  self.trail_height = self.trail.get_size()
        self.square_surf = pygame.Surface((self.trail_width, self.trail_height), pygame.SRCALPHA)
        self.frame_left = 10
        self.trail_list = []

    def draw(self, screen: Surface):
        pos_x = self.generator.properties[KEY_POS_X]
        pos_y = self.generator.properties[KEY_POS_Y]

        if self.frame_left == 0:
            self.frame_left = 10
            self.trail_list.append([pos_x,pos_y])
            if len(self.trail_list) >= 11 :
                self.trail_list.pop(0)
        else:
            self.frame_left -= 1

        for i in self.trail_list :
            screen.blit(self.trail, (self.trail_width / 2 + i[0], self.trail_height / 2 + i[1]))

        # Faire tourner la surface contenant le carré
        #rotated_surf = pygame.transform.rotate(self.square_surf, self.get_rotation())
       # rotated_rect = rotated_surf.get_rect(center=(pos_x, pos_y))

        # Afficher la surface tournée sur l’écran principal
      #  rotated_rect = rotated_rect.move(self.trail_width, self.trail_height)

        #screen.blit(rotated_surf, rotated_rect)

    def update_position(self, delta_time: float):
        pass

    def move(self, distance: float):
        pass

    def set_rotation(self, angle):
        pass

    def get_rotation(self):
        pass
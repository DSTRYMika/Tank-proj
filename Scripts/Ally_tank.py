import pygame
import math
from pygame import Surface
from Draw import Drawable
from Level import Level
from Scripts.FixedStrings import KEY_POS_X, KEY_POS_Y, KEY_ROT

WIDTH,HEIGHT = 600,400

class Ally_tank (Drawable) :

    def __init__(self) :
        Drawable.__init__(self)
        self.velocity_x: float = 0.0
        self.velocity_y: float = 0.0
        self.friction = 0.92
        self.tank = pygame.image.load("ally.png")
        self.tank_width , self.tank_height = self.tank.get_size()
        self.rect = pygame.Rect(0, 0, self.tank_width, self.tank_height)
        square_size = 200
        self.square_surf = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
        self.square_rect = self.square_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    def draw(self,screen: Surface):

        pos_x=self.properties[KEY_POS_X]
        pos_y=self.properties[KEY_POS_Y]
        # tank
        self.square_surf.blit(self.tank,(self.tank_width/2,self.tank_height/2))

        # Faire tourner la surface contenant le carré
        rotated_surf = pygame.transform.rotate(self.square_surf, self.get_rotation())
        rotated_rect = rotated_surf.get_rect(center=(pos_x, pos_y))

        # Afficher la surface tournée sur l’écran principal
        rotated_rect=rotated_rect.move(self.tank_width,self.tank_height)

        screen.blit(rotated_surf, rotated_rect)

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
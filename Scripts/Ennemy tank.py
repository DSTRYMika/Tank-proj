import pygame
import math
from pygame import Surface
from Draw import Drawable
WIDTH,HEIGHT = 600,400

class Ennemy_tank (Drawable) :

    def __init__(self) :
        self.pos_x = 10
        self.pos_y = 10
        self.angle = 0
        self.tank = pygame.image.load("Ennemy.png") #image needs to be changed
        self.tank_width , self.tank_height = self.tank.get_size()
        self.rect = pygame.Rect(0, 0, self.tank_width, self.tank_height)
        square_size = 200
        self.square_surf = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
        self.square_rect = self.square_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    def set_rotation(self, angle):
        self.angle = angle

    def draw(self,screen: Surface):

        # tank
        self.square_surf.blit(self.tank,(self.tank_width/2,self.tank_height/2))

        # Faire tourner la surface contenant le carré
        print(self.angle)
        rotated_surf = pygame.transform.rotate(self.square_surf, self.angle)
        rotated_rect = rotated_surf.get_rect(center=(self.pos_x, self.pos_y))

        # Afficher la surface tournée sur l’écran principal
        rotated_rect=rotated_rect.move(self.tank_width,self.tank_height)
        screen.blit(rotated_surf, rotated_rect)

    def Move (self,speed) :
        delta_y= math.cos(self.angle/180* 3.14159) * speed
        delta_x = math.sin(self.angle/180* 3.14159) * speed
        self.pos_x -= delta_x
        self.pos_y -= delta_y

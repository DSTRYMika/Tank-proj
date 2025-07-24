import pygame
from pyglet.image.codecs.gif import read_table_based_image

from Scripts.Draw import Drawable

WIDTH, HEIGHT = 600, 400
class Enemy_tank (Drawable) :
    def __init__(self, width, height,x: int, y: int) :
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(0, 0, width, height)
        self.angle = 0

    def set_rotation(self, angle):
        if angle >= 360 :
            angle = angle - 360
            self.angle = angle
        else :
            self.angle = angle

    def image_by_angle (self) :

        if 337.5 < self.angle <= 360 or 0 < self.angle <= 22.5 :
            self.angle = 0
        elif 22.5 < self.angle <= 67.5 :
            self.angle = 45
        elif 67.5 < self.angle <= 112.5:
            self.angle =  90
        elif 112.5 < self.angle <= 157.5:
            self.angle =  135
        elif 157.5 < self.angle <= 202.5:
            self.angle =  180
        elif 202.5 < self.angle <= 247.5:
            self.angle =  215
        elif 247.5 < self.angle <= 292.5:
            self.angle = 260
        elif 292.5 < self.angle <= 337.5:
            self.angle =  305
        else : raise ValueError("L'angle doit etre compris entre 0 et 360 degres")

    def draw(self,pygame: pygame, screen: pygame.Surface):


        tank = pygame.image.load("/Sprites/pas gentil/1.jpg")

        # Surface pour le carré (plus grand pour éviter les coupures lors de la rotation)
        square_size = 100
        self.square_surf = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
        self.square_rect = self.square_surf.get_rect(center=(WIDTH//2, HEIGHT//2))

        # tank
        screen.blit(tank,(100,100))

        # Faire tourner la surface contenant le carré
        rotated_surf = pygame.transform.rotate(self.square_surf, self.angle)
        rotated_rect = rotated_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Afficher la surface tournée sur l’écran principal
        rotated_rect=rotated_rect.move(self.x, self.y)

        screen.blit(rotated_surf, rotated_rect)
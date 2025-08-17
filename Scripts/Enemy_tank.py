import pygame
import math
from pygame import Surface
from Draw import Drawable
from Scripts.Ally_tank import Ally_tank

WIDTH,HEIGHT = 600,400

class Enemy_tank (Ally_tank) :

    def __init__(self, width, height,x: int, y: int,screen : pygame.display) :
        super().__init__(self,width,height,x,y,pygame.display)
        self.tank = pygame.image.load("Ennemy.png")



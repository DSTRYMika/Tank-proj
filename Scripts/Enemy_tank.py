import pygame
import math
from pygame import Surface
from Draw import Drawable
from Scripts.Ally_tank import Ally_tank
from Scripts.FixedStrings import KEY_POS_X, KEY_POS_Y

WIDTH,HEIGHT = 600,400

class Enemy_tank (Ally_tank) :

    def __init__(self) :
        super().__init__()
        self.tank = pygame.image.load("../Sprites/Enemy.png")

    def update_position(self, delta_time: float):
        self.properties[KEY_POS_X] += delta_time * 10
        self.properties[KEY_POS_Y] += delta_time * 10


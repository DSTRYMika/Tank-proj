import pygame
import random
from Scripts.Ally_tank import Ally_tank
from Scripts.Draw import Drawable
from Scripts.EntityMover import EntityMover
from Scripts.FixedStrings import KEY_POS_X, KEY_POS_Y, KEY_ROT

class Enemy_tank(Ally_tank):

    def __init__(self, target : Drawable):
        super().__init__()
        self.pset_x(random.randint(0,500))
        self.pset_y(random.randint(0,500))
        self.target=target
        self.em: EntityMover = EntityMover(self.pget_x(),self.pget_y())
        self.tank = pygame.image.load("../Sprites/Enemy.png")

    def update_position(self, delta_time: float):
        self.em.update_position(self.target.properties[KEY_POS_X], self.target.properties[KEY_POS_Y])
        x, y = self.em.get_position()
        self.properties[KEY_POS_X] = x
        self.properties[KEY_POS_Y] = y
        self.properties[KEY_ROT] = self.em.get_orientation()

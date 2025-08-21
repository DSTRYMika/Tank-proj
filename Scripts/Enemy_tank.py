import pygame
from Scripts.Ally_tank import Ally_tank
from Scripts.EntityMover import EntityMover

WIDTH, HEIGHT = 600, 400


class Enemy_tank(Ally_tank):

    def __init__(self):
        super().__init__()
        self.x: float = 0
        self.y: float = 0
        self.em: EntityMover = EntityMover(self.x, self.y)
        self.tank = pygame.image.load("../Sprites/Enemy.png")

    def update_position(self, delta_time: float):
        pass

    def MoverCall(self, target_x: float, target_y: float()):
        self.em.update_position(100, 100)
        self.x,self.y = self.em.get_position()
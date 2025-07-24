import pygame
import math

class Movements():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.movement_speed = 1
    def Move (self,event):
        if event.type == pygame.KEYDOWN:
            angle_rad = math.radians(self.rotation)
            dx = math.cos(angle_rad) * self.movement_speed
            dy = math.sin(angle_rad) * self.movement_speed
            self.x = self.x - dx
            self.y = self.y - dy
        elif event.type == pygame.KEYUP:
            angle_rad = math.radians(self.rotation)
            dx = math.cos(angle_rad) * self.movement_speed
            dy = math.sin(angle_rad) * self.movement_speed
            self.x = self.x + dx
            self.y = self.y + dy
        elif event.type == pygame.BUTTON_RIGHT :
            self.rotation = self.rotation - 1
        elif event.type == pygame.BUTTON_LEFT :
            self.rotation = self.rotation + 1
        else :
            pass
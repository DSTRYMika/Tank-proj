from abc import ABC, abstractmethod
import pygame
from pygame import Surface

from Scripts.FixedStrings import *


class Drawable(ABC):
    def __init__(self):
        self.properties: dict = {}
        self.properties[KEY_ROT] = 0
        self.properties[KEY_POS_X] = 0
        self.properties[KEY_POS_Y] = 0

    @abstractmethod
    def draw(self, screen: Surface):
        pass

    @abstractmethod
    def update_position(self, delta_time: float):
        pass

    @abstractmethod
    def move(self, distance: float):
        pass

    @abstractmethod
    def set_rotation(self, angle):
        self.properties[KEY_ROT] = angle

    @abstractmethod
    def get_rotation(self):
        return self.properties[KEY_ROT]

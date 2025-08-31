from abc import ABC, abstractmethod
from typing import Optional, Tuple

import pygame
from pygame import Surface

from Scripts.FixedStrings import *


class Drawable(ABC):
    def __init__(self):
        self.properties: dict = {}
        self.properties[KEY_ROT] = 0
        self.properties[KEY_POS_X] = 0
        self.properties[KEY_POS_Y] = 0

    def pget_x(self) -> int:
        return self.properties[KEY_POS_X]

    def pget_y(self) -> int:
        return self.properties[KEY_POS_Y]

    def pset_x(self, x: int) -> None:
        self.properties[KEY_POS_X]=x

    def pset_y(self, y: int) -> None:
        self.properties[KEY_POS_Y]=y

    @abstractmethod
    def draw(self, screen: Surface):
        pass

    def get_trail_emitter(self) -> tuple[int, str] | None:
        return None

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

    def MoverCall(self, target_x: float, target_y: float()):
        pass



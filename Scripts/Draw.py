from abc import ABC
import pygame
from pygame import Surface

from Scripts.FixedStrings import *


class Drawable (ABC) :
    def __init__(self,):
        self.properties: dict = {}
        self.properties[KEY_ROT]=0
        self.properties[KEY_POS_X]=0
        self.properties[KEY_POS_Y]=0

    def draw (self,screen: Surface) :
        pass

    def update_position(self, is_moving: bool):
        pass

    def move (self,distance : float):
        pass

    def set_rotation(self, angle):
        self.properties[KEY_ROT]=angle

    def get_rotation(self):
        return self.properties[KEY_ROT]

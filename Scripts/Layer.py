from pygame import Surface

from Draw import Drawable
from Scripts.FixedStrings import *


class Layer (Drawable) :

    def __init__(self):
        super().__init__()
        self.layer: list[Drawable] = []

    def draw(self, screen: Surface):
        one: Drawable
        for one in self.layer:
            one.draw(screen)

    def update_position(self, delta_time: float):
        one: Drawable
        for one in self.layer:
            one.update_position(delta_time)

    def move(self, distance: float):
        one: Drawable
        for one in self.layer:
            one.update_position(distance)

    def add_drawable(self, name: str, pos_x: int, pos_y: int, drawable: Drawable):
        drawable.properties[KEY_NAME] = name
        drawable.properties[KEY_POS_X] = pos_x
        drawable.properties[KEY_POS_Y] = pos_y
        self.layer.append(drawable)

from Scripts.Draw import Drawable
from Scripts.FixedStrings import *


class Level :
    def __init__(self):
        self.drawables : list[Drawable] = []

    def add_drawable(self,name: str, pos_x: int, pos_y: int,drawable: Drawable) :
        drawable.properties[KEY_NAME] = name
        drawable.properties[KEY_POS_X] = pos_x
        drawable.properties[KEY_POS_Y] = pos_y
        self.drawables.append(drawable)

    def get_drawable(self, name :str) -> Drawable | None:
        for drawable in self.drawables:
            if drawable.properties[KEY_NAME] == name:
                return drawable
        return None

    def get_drawables(self)->list[Drawable]:
        return self.drawables



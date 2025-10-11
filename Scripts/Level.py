from Scripts.Draw import Drawable
from Scripts.FixedStrings import *
from Scripts.Layer import Layer


class Level :
    def __init__(self):
        self.drawables : list[Drawable] = []

    def add_drawable(self,name: str, pos_x: int, pos_y: int,drawable: Drawable) :
        drawable.properties[KEY_NAME] = name
        drawable.properties[KEY_POS_X] = pos_x
        drawable.properties[KEY_POS_Y] = pos_y
        self.drawables.append(drawable)

    def get_drawable(self, name :str) -> Drawable | None:
        return self._get_drawable_from_list(self.drawables,name)

    def _get_drawable_from_list(self,list : list[Drawable], name :str):
        drawable: Drawable
        for drawable in list:
            if drawable.properties[KEY_NAME] == name:
                return drawable
        for drawable in list:
            if drawable.has_sub_drawables():
                return self._get_drawable_from_list(drawable.get_sub_drawables(),name)
        return None

    def get_drawables(self)->list[Drawable]:
        return self.drawables



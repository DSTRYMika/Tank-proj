import pygame.font

from Layer import Layer
from Scripts import FixedStrings
from Scripts.Ally_tank import Ally_tank
from Scripts.Draw import Drawable
from Scripts.Enemy_tank import Enemy_tank
from Scripts.Fps_counter import Fps_Counter
from Scripts.Level import Level
from Scripts.Trail import Trail

import random
from Scripts.FixedStrings import *

# Define the grid manager
class LevelBuilder:
    def __init__(self) -> None:
        self.frame_until_trail = 10

    def get_layer(self, name: str) -> Layer:
        found: Layer| None = level.get_drawable(name)
        if not found:
            found = Layer()
            level.add_drawable(name,0,0,found)
        return found

    def layer_bg(self)-> Layer:
        return self.get_layer(FixedStrings.KEY_LAYER_BACKGROUND)

    def layer_entities(self)-> Layer:
        return self.get_layer(FixedStrings.KEY_LAYER_ENTITIES)

    def layer_entities1(self)-> Layer:
        return self.get_layer(FixedStrings.KEY_LAYER_ENTITIES_1)

    def layer_UI(self)-> Layer:
        return self.get_layer(FixedStrings.KEY_LAYER_UI)

    def layer_Menu(self)-> Layer:
        return self.get_layer(FixedStrings.KEY_LAYER_MENU)


    def build_level(self, level: Level) -> None:

        new_ally: Ally_tank = Ally_tank()
        new_enemy: Drawable = Enemy_tank(new_ally)
        self.layer_entities().add_drawable(VAL_ALLY, 100, 100, new_ally)
        level.add_drawable(VAL_ENEMY, new_enemy.pget_x(),new_enemy.pget_y(), new_enemy)

        new_trail = Trail(new_ally)
        new_ennemy_trail = Trail(new_enemy)
        fps_counter = Fps_Counter()
        level.add_drawable("Ennemy_trail",0,0,new_ennemy_trail )
        level.add_drawable("Trail", 100, 100, new_trail)
        level.add_drawable("Fps_Counter", 0,0,fps_counter)

        for i in range(5) :
            new_enemy : Drawable = Enemy_tank(new_ally)
            new_ennemy_trail = Trail(new_enemy)
            level.add_drawable(VAL_ENEMY, new_enemy.pget_x(), new_enemy.pget_y(), new_enemy)
            level.add_drawable("Ennemy_trail", 0, 0, new_ennemy_trail)
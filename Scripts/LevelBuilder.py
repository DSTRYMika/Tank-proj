from typing import Optional

from Scripts.Ally_tank import Ally_tank
from Scripts.Draw import Drawable
from Scripts.Enemy_tank import Enemy_tank
from Scripts.Level import Level
from Scripts.Trail import Trail
from StateType import StateType

import random
from Scripts.FixedStrings import *


# Define the grid manager
class LevelBuilder:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid: list[list[StateType]] = [
            [StateType.Undefined for _ in range(width)] for _ in range(height)
        ]
        self.frame_until_trail = 10

    def set_item(self, x: int, y: int, item: StateType) -> None:
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = item

    def get_item(self, x: int, y: int) -> Optional[StateType]:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def build_level(self, level: Level) -> None:
        new_ally: Drawable = Ally_tank()
        new_enemy: Drawable = Enemy_tank()
        level.add_drawable(VAL_ALLY, 100, 100, new_ally)
        level.add_drawable(VAL_ENEMY, 200, 100, new_enemy)

        new_trail = Trail(new_ally)
        level.add_drawable("Trail", 100, 100, new_trail)

        # self.new_ally.set_rotation(40)
        # self.second_tank = Ally_tank()

# level1 = ItemGrid(10,10)
#
# for y in range(level1.width) :
#     for i in range(level1.height) :
#         x = random.randint(0,100)
#         if x <= 70 :
#             level1.set_item(y,i,StateType.Undefined)
#         if 70 < x <= 90:
#             level1.set_item(y,i,StateType.TRAP)
#
# print_out = ""
# iteration = 1
# for i in range(level1.width) :
#     for y in range(level1.height) :
#         if level1.get_item(i,y) == StateType.Undefined :
#             print_out += "🟢"
#         elif level1.get_item(i,y) == StateType.TRAP :
#             print_out += "🔴"
#         if iteration == 10 :
#             print_out += "\n"
#             iteration = 1
#         else :
#             iteration += 1
#
# print(print_out)
#
# print(level1.get_item(3,9))

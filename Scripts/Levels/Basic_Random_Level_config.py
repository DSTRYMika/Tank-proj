from typing import Optional
import random
from Scripts.StateType import StateType

class Basic_Random_Level:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: list[list[StateType]] = [
            [StateType.Undefined for _ in range(width)] for _ in range(height)
        ]

    def create_random_grid(self):

        for y in range(self.width):
            for i in range(self.height):
                x = random.randint(0, 100)
                if x <= 70:
                    self.set_item(y, i, StateType.Undefined)

                if 70 < x <= 90:
                    self.set_item(y, i, StateType.TRAP)

    def set_item(self, x: int, y: int, item: StateType) -> None:
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = item

    def get_item(self, x: int, y: int) -> Optional[StateType]:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

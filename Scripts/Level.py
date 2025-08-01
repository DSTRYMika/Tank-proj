import pygame

class Level :
    def __init__(self):
        self.drawables = []

    def add_drawables(self, screen: pygame.Surface,pos : list = [0,0],object: str = None) :
        obj = dict()
        obj["screen"] = screen
        obj["pos"] = pos
        obj["image"] = object
        self.drawables.append(obj)

    def draw_drawables(self) -> None:
        for obj in self.drawables:
            screen = obj["screen"]
            image = obj["image"]
            pos = obj["pos"]
            screen.blit(image, pos)


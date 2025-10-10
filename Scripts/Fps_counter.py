from pygame import Surface
import pygame

from Draw import Drawable


class Fps_Counter(Drawable):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 30)
        self.text_surface = self.font.render("FPS:", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()

    def draw(self, screen: Surface):
        screen.blit(self.text_surface, self.text_rect)

    def update_position(self, delta_time: float):
        pass

    def move(self, distance: float):
        pass

    def Get_Fps(self):
        pass
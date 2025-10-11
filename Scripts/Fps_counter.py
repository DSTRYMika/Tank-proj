import time

from pygame import Surface
import pygame

from Draw import Drawable
import threading


class Fps_Counter(Drawable):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.Font(None, 30)
        self.text = ""
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()
        self.frame_for_current_second = 0
        self.previous_frame_time=0
        self.fps_history: list = []
        self.fps_counter = 0
        self.current_fps_counter = 0

    def draw(self, screen: Surface):
        screen.blit(self.text_surface, self.text_rect)

    def update_position(self, delta_time: float):
        self.frame_for_current_second += 1
        now = pygame.time.get_ticks()
        duration= now-self.previous_frame_time
        self.current_fps_counter= 1000 / duration
        self.text = "FPS:" + str(int(self.fps_counter))
        self.fps_history.append(self.current_fps_counter)
        if len(self.fps_history) > 10 :
            self.fps_history.pop(0)
        for i in self.fps_history :
            self.fps_counter += i
        self.fps_counter = self.fps_counter / len(self.fps_history)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect()

        self.previous_frame_time = now


    def move(self, distance: float):
        pass

    def Get_Fps(self):
        pass


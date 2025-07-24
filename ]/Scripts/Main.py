from pickletools import pyfloat

import pygame
import math

from Ally_tank import Ally_tank
from Draw import Drawable
from Rectangle import Rectangle

liste: list[Rectangle] = []

def Remplir_liste (Nombre_de_rectangle: int,screen_width:int,screen_height:int) :
    from random import randint
    #for i in range(Nombre_de_rectangle):
    #    rect = Rectangle(50,50,randint(20, 100), randint(20, 100))
   #     rect.rect.x = randint(0, screen_width - rect.width)
    #    rect.rect.y = randint(0, screen_height - rect.height)
     #   liste.append(rect)




if __name__ == '__main__':
    pygame.init()

    WIDTH, HEIGHT = 600, 400
    square_size = 100
    square_surf = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rotation carrée sur surface séparée")
    new_ally = Ally_tank(100,100,100,100)
    new_ally.set_rotation(40)

    clock = pygame.time.Clock()

    # Dessiner le carré sur cette surface (rempli en rouge)
    pygame.draw.rect(square_surf, (255, 0, 0), (0, 0, square_size, square_size))
    Remplir_liste(5, WIDTH, HEIGHT)

    angle = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        angle += 1  # degrés

        # Nettoyer écran principal
        screen.fill((30, 30, 30))

        Ally_tank.draw(new_ally)

        for rect in liste:
            rect.set_rotation(angle)
            rect.draw(pygame, screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

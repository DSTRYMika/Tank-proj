import pygame
from Ally_tank import Ally_tank
from Scripts.FixedStrings import VAL_ALLY
from Scripts.Level import Level
from LevelBuilder import LevelBuilder

class Game_Engine :
    def __init__(self):
        self.rotation = 0
        pygame.init()
        pygame.key.set_repeat()
        self.WIDTH, self.HEIGHT = 600, 400
        self.square_size = 100
        self.square_surf = pygame.Surface((self.square_size, self.square_size), pygame.SRCALPHA)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Rotation carrée sur surface séparée")
        self.clock = pygame.time.Clock()
        self.current_level=Level()

        builder=LevelBuilder(400,400)
        builder.build_level(self.current_level)

    def draw_level(self):
        drawables=self.current_level.get_drawables()
        for d in drawables:
            d.draw(self.screen)

    def Run (self) :
        # Dessiner le carré sur cette surface (rempli en rouge)
        pygame.draw.rect(self.square_surf, (255, 0, 0), (0, 0, self.square_size, self.square_size))
        # Remplir_liste(5, WIDTH, HEIGHT)
        running = True
        new_ally = self.current_level.get_drawable(VAL_ALLY)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                new_ally.set_rotation(new_ally.get_rotation() +2)
            elif keys[pygame.K_RIGHT]:
                new_ally.set_rotation(new_ally.get_rotation() - 2)
            elif keys[pygame.K_DOWN]:
                new_ally.move(-2)
            elif keys[pygame.K_UP]:
                new_ally.move(+2)
            new_ally.update_position(self.clock.tick(60) / 1000)
            # Nettoyer écran principal
            self.screen.fill((30, 30, 30))
            self.draw_level()

            pygame.display.flip()
            self.clock.tick(60)
    def Stop (self) :
        pygame.quit()

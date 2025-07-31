import pygame
from Ally_tank import Ally_tank

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
        self.new_ally = Ally_tank()
        self.new_ally.set_rotation(40)
        self.second_tank = Ally_tank()
        self.clock = pygame.time.Clock()

    def Run (self) :
        # Dessiner le carré sur cette surface (rempli en rouge)
        pygame.draw.rect(self.square_surf, (255, 0, 0), (0, 0, self.square_size, self.square_size))
        # Remplir_liste(5, WIDTH, HEIGHT)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.rotation += 1

                if event.key == pygame.K_RIGHT:
                    self.rotation -= 1
                if event.key == pygame.K_DOWN:
                    Ally_tank.Move(self.new_ally, 2)
                if event.key == pygame.K_UP:
                    Ally_tank.Move(self.new_ally, -2)

            # Nettoyer écran principal
            self.screen.fill((30, 30, 30))
            Ally_tank.set_rotation(self.new_ally, self.rotation)
            Ally_tank.draw(self.new_ally, self.screen)

            pygame.display.flip()
            self.clock.tick(60)
    def Stop (self) :
        pygame.quit()

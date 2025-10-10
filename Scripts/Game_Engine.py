import pygame
from Scripts.Draw import Drawable
from Scripts.FixedStrings import VAL_ALLY, KEY_NAME, KEY_POS_X, KEY_POS_Y
from Scripts.Level import Level
from LevelBuilder import LevelBuilder

class Game_Engine :
    def __init__(self):
        self.DEBUG: bool = False
        self.rotation = 0
        pygame.init()
        pygame.key.set_repeat()
        self.WIDTH, self.HEIGHT = 1000, 980
        self.square_size = 100
        self.square_surf = pygame.Surface((self.square_size, self.square_size), pygame.SRCALPHA)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Rotation carrée sur surface séparée")
        self.clock = pygame.time.Clock()
        self.current_level = Level()

        builder = LevelBuilder()
        builder.build_level(self.current_level)


    def move_level(self):
        delta: float = self.clock.tick(60) / 1000
        drawables=self.current_level.get_drawables()
        for d in drawables:
            d.update_position(delta)


    def draw_level(self):
        drawables : list[Drawable]=self.current_level.get_drawables()
        if self.DEBUG:
            print("DRAW_DEBUG #  ---- new frame ----")

        for d in drawables:
            if self.DEBUG:
                print(f"DRAW_DEBUG # {d.properties[KEY_NAME]}  x={d.properties[KEY_POS_X]}  y={d.properties[KEY_POS_Y]}")

            d.draw(self.screen)

    def Run (self) :

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

            self.move_level()
            # Nettoyer écran principal
            self.screen.fill((30, 30, 30))
            self.draw_level()

            pygame.display.flip()
            self.clock.tick(60)

    def Stop (self) :
        pygame.quit()


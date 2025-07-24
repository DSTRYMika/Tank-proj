import pygame
from Draw import Drawable

WIDTH, HEIGHT = 600, 400
class Rectangle (Drawable) :
    def __init__(self, width, height,x: int, y: int) :
        self.x = x
        self.y = y
        self.rect = pygame.Rect(0, 0, width, height)
        self.angle = 0

    def set_rotation(self, angle):
        self.angle = angle

    def draw(self,pygame: pygame, screen: pygame.Surface):

        # Surface pour le carré (plus grand pour éviter les coupures lors de la rotation)
        square_size = 100
        self.square_surf = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
        self.square_rect = self.square_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
        pygame.draw.rect(self.square_surf, (255, 0, 0), (0, 0, square_size, square_size))

        # Faire tourner la surface contenant le carré
        rotated_surf = pygame.transform.rotate(self.square_surf, self.angle)
        rotated_rect = rotated_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Afficher la surface tournée sur l’écran principal
        rotated_rect=rotated_rect.move(self.x, self.y)

        screen.blit(rotated_surf, rotated_rect)



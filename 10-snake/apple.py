import pygame

from constants import BLOCK_SIZE, ORANGE


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(surface, ORANGE, rect)

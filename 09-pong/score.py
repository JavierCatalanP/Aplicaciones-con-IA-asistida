# score.py
import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self, font, x, y):
        super().__init__()
        self.score = 0
        self.font = font
        self.x = x
        self.y = y

    def update(self):
        self.image = self.font.render(str(self.score), True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def increment(self):
        self.score += 1

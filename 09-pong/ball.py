# ball.py
import pygame
from constants import BALL_SIZE


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BALL_SIZE, BALL_SIZE])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.init_speed()

    def init_speed(self):
        self.speed_x = 3  # Reduce the initial speed of the ball
        self.speed_y = 3  # Reduce the initial speed of the ball

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.init_speed()

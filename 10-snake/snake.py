import pygame

from constants import BLOCK_SIZE, WHITE


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = BLOCK_SIZE
        self.dy = 0
        self.body = [(x, y), (x - BLOCK_SIZE, y), (x - 2 * BLOCK_SIZE, y)]

    def draw(self, surface):
        for block in self.body:
            rect = pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(surface, WHITE, rect)

    def move(self):
        # Actualizar la posición de la cabeza
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))

        # Eliminar la última parte del cuerpo
        self.body.pop()

    def check_collision(self):
        # Comprobar si la cabeza de la serpiente se superpone con cualquier parte del cuerpo, excepto la cola
        for block in self.body[1:-1]:
            if self.body[0] == block:
                return True
        return False

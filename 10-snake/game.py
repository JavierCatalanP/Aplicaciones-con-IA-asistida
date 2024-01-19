import pygame
import random

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, BLACK, WHITE, ORANGE, SNAKE_SPEED
from snake import Snake
from apple import Apple


class Game:
    def __init__(self):
        # Crear la ventana
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Crear la serpiente
        self.snake = Snake(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        # Crear el objetivo
        self.apple = Apple(random.randint(0, SCREEN_WIDTH - BLOCK_SIZE), random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE))

        # Puntuación inicial
        self.score = 0

    def run(self):
        # Bucle principal del juego
        running = True
        clock = pygame.time.Clock()

        while running:
            # Procesar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.dx = 0
                        self.snake.dy = -BLOCK_SIZE
                    elif event.key == pygame.K_DOWN:
                        self.snake.dx = 0
                        self.snake.dy = BLOCK_SIZE
                    elif event.key == pygame.K_LEFT:
                        self.snake.dx = -BLOCK_SIZE
                        self.snake.dy = 0
                    elif event.key == pygame.K_RIGHT:
                        self.snake.dx = BLOCK_SIZE
                        self.snake.dy = 0

            # Mover la serpiente
            self.snake.move()

            # Comprobar si la serpiente ha chocado con una pared o consigo misma
            if self.snake.x < 0 or self.snake.x > SCREEN_WIDTH - BLOCK_SIZE or self.snake.y < 0 or self.snake.y > SCREEN_HEIGHT - BLOCK_SIZE or self.snake.check_collision():
                running = False

            # Comprobar si la serpiente ha comido la manzana
            apple_rect = pygame.Rect(self.apple.x, self.apple.y, BLOCK_SIZE, BLOCK_SIZE)
            if apple_rect.collidepoint(*self.snake.body[0]):
                self.score += 1
                self.snake.body.append(self.snake.body[-1])
                self.apple = Apple(random.randint(0, SCREEN_WIDTH - BLOCK_SIZE),
                                   random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE))

            # Dibujar en la pantalla
            self.screen.fill(BLACK)
            self.snake.draw(self.screen)
            self.apple.draw(self.screen)

            # Mostrar la puntuación
            font = pygame.font.SysFont("Arial", 20)
            score_text = font.render("Score: " + str(self.score), True, WHITE)
            self.screen.blit(score_text, (10, 10))

            # Actualizar la pantalla
            pygame.display.flip()

            # Limitar la velocidad de la serpiente
            clock.tick(SNAKE_SPEED)

        # Cerrar Pygame
        pygame.quit()

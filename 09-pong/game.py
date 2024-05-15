# game.py
import pygame
import random
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from paddle import Paddle
from ball import Ball
from score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

    def run(self):
        player_paddle = Paddle(20, SCREEN_HEIGHT // 2 - 30)
        ai_paddle = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - 30)
        ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        player_score = Score(self.font, SCREEN_WIDTH // 2 - 60, 10)
        ai_score = Score(self.font, SCREEN_WIDTH // 2 + 40, 10)

        all_sprites = pygame.sprite.Group(player_paddle, ai_paddle, ball)
        scores = pygame.sprite.Group(player_score, ai_score)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                player_paddle.move_up()
            if keys[pygame.K_DOWN]:
                player_paddle.move_down()

            # Simple AI movement with randomness
            if random.random() < 0.975:  # 97.5% chance of following the ball
                if ball.rect.y > ai_paddle.rect.y:
                    ai_paddle.move_down()
                else:
                    ai_paddle.move_up()
                    
            # Add a delay before the ball starts moving
            if ball.rect.x == SCREEN_WIDTH // 2 and ball.rect.y == SCREEN_HEIGHT // 2:
                pygame.time.delay(1500)  # Delay in milliseconds

            ball.update()
            scores.update()

            # Check for collisions and scoring
            if pygame.sprite.collide_rect(ball, player_paddle) or pygame.sprite.collide_rect(ball, ai_paddle):
                ball.speed_x = -ball.speed_x

            if ball.rect.y <= 0 or ball.rect.y >= SCREEN_HEIGHT - ball.rect.height:
                ball.speed_y = -ball.speed_y

            if ball.rect.x <= 0:
                ai_score.increment()
                ball.rect.x = SCREEN_WIDTH // 2
                ball.rect.y = SCREEN_HEIGHT // 2

            if ball.rect.x >= SCREEN_WIDTH - ball.rect.width:
                player_score.increment()
                ball.rect.x = SCREEN_WIDTH // 2
                ball.rect.y = SCREEN_HEIGHT // 2

            self.screen.fill((0, 0, 0))
            all_sprites.draw(self.screen)
            scores.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

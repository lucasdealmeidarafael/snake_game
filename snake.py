import pygame
from pygame.locals import *
import random


WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
STARTING_POS_X = WINDOWS_WIDTH / 2
STARTING_POS_Y = WINDOWS_HEIGHT / 2
BLOCK = 10

def checking_margins(pos):
    if 0 <= pos[0] < WINDOWS_WIDTH and 0 <= pos[1] < WINDOWS_HEIGHT:
        return False
    else:
        return True
    
def generate_random_position():
    x = random.randint(0, WINDOWS_WIDTH)
    y = random.randint(0, WINDOWS_HEIGHT)

    return x // BLOCK * BLOCK, y // BLOCK * BLOCK
def game_over():
    pygame.quit()
    quit()

pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))

snake_pos = [(STARTING_POS_X, STARTING_POS_Y)]
snake_surface = pygame.Surface((BLOCK, BLOCK))
snake_surface.fill((255, 255, 255))
direction = K_LEFT

apple_surface = pygame.Surface((BLOCK, BLOCK))
apple_surface.fill((255, 0, 0))
apple_pos = generate_random_position()

while True:
    pygame.time.Clock().tick(30)
    window.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                direction = event.key

    window.blit(apple_surface, apple_pos)

    for pos in snake_pos:
        window.blit(snake_surface,pos)

    if checking_margins(snake_pos[0]):
        game_over()

    if direction == K_RIGHT:
        snake_pos[0] = snake_pos[0][0] + BLOCK, snake_pos[0][1] # Movimentação para a direita.

    elif direction == K_LEFT:
        snake_pos[0] = snake_pos[0][0] - BLOCK, snake_pos[0][1] # Movimentação para a esquerda.

    elif direction == K_UP:
        snake_pos[0] = snake_pos[0][0], snake_pos[0][1] - BLOCK # Movimentação para cima.

    elif direction == K_DOWN:
        snake_pos[0] = snake_pos[0][0], snake_pos[0][1] + BLOCK # Movimentação para baixo.
    pygame.display.update()
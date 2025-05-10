import pygame
from pygame.locals import *

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
STARTING_POS_X = WINDOWS_WIDTH / 2
STARTING_POS_Y = WINDOWS_HEIGHT / 2
BLOCK = 10

pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))

snake_pos = [(STARTING_POS_X, STARTING_POS_Y)]
snake_surface = pygame.Surface((BLOCK, BLOCK))
snake_surface.fill((255, 255, 255))
direction = K_LEFT

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

    for pos in snake_pos:
        window.blit(snake_surface,pos)

    if direction == K_RIGHT:
        snake_pos[0] = snake_pos[0][0] + BLOCK, snake_pos[0][1] # Movimentação para a direita.

    elif direction == K_LEFT:
        snake_pos[0] = snake_pos[0][0] - BLOCK, snake_pos[0][1] # Movimentação para a esquerda.

    elif direction == K_UP:
        snake_pos[0] = snake_pos[0][0], snake_pos[0][1] - BLOCK # Movimentação para cima.

    elif direction == K_DOWN:
        snake_pos[0] = snake_pos[0][0], snake_pos[0][1] + BLOCK # Movimentação para baixo.
    pygame.display.update()
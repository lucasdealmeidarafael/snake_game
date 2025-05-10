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

while True:
    window.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    for pos in snake_pos:
        window.blit(snake_surface,pos)

    pygame.display.update()
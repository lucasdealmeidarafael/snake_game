import pygame
from pygame.locals import *

import random
import time

WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
STARTING_POS_X = WINDOWS_WIDTH / 2
STARTING_POS_Y = WINDOWS_HEIGHT / 2
BLOCK = 10

points = 0
velocity = 10

pygame.font.init()
fonte = pygame.font.SysFont('arial', 35, True, True) # Negrito e Itálico.

def collision(pos1, pos2):
    return pos1 == pos2

def checking_margins(pos):
    if 0 <= pos[0] < WINDOWS_WIDTH and 0 <= pos[1] < WINDOWS_HEIGHT:
        return False
    else:
        return True
    
def generate_random_position():
    x = random.randint(0, WINDOWS_WIDTH)
    y = random.randint(0, WINDOWS_HEIGHT)

    if (x,y) in obstacle_pos:
        generate_random_position()

    return x // BLOCK * BLOCK, y // BLOCK * BLOCK
def game_over():
    fonte = pygame.font.SysFont('arial', 60, True, True)
    gameOver = 'GAME OVER'
    text_over = fonte.render(gameOver, True, (255,255,255))
    window.blit(text_over,(110,300))
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()

pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
pygame.display.set_caption('Sna Snake')

snake_pos = [(STARTING_POS_X, STARTING_POS_Y), (STARTING_POS_X + BLOCK, STARTING_POS_Y), (STARTING_POS_X + 2 * BLOCK, STARTING_POS_Y)]
snake_surface = pygame.Surface((BLOCK, BLOCK))
snake_surface.fill((255, 255, 255))
direction = K_LEFT

obstacle_pos = []
obstacle_surface = pygame.Surface((BLOCK, BLOCK))
obstacle_surface.fill((82, 82, 82))

apple_surface = pygame.Surface((BLOCK, BLOCK))
apple_surface.fill((255, 0, 0))
apple_pos = generate_random_position()

while True:
    pygame.time.Clock().tick(velocity)
    window.fill((0,0,0))

    message = f'Points: {points}'
    text = fonte.render(message, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                if event.key == K_UP and direction == K_DOWN:
                    continue
                elif event.key == K_DOWN and direction == K_UP:
                    continue
                elif event.key == K_RIGHT and direction == K_LEFT:
                    continue
                elif event.key == K_LEFT and direction == K_RIGHT:
                    continue
                else:
                    direction = event.key

    window.blit(apple_surface, apple_pos)

    if (collision(snake_pos[0], apple_pos)):
        snake_pos.append((-10,-10))
        apple_pos = generate_random_position()
        obstacle_pos.append(generate_random_position())
        points += 1
        if points % 5 == 0:
            velocity += 2

    for pos in obstacle_pos:
        if collision(snake_pos[0],pos):
            game_over()
        window.blit(obstacle_surface, pos)
    
    for pos in snake_pos:
        window.blit(snake_surface,pos)

    for item in range(len(snake_pos)-1,0,-1):
        if collision(snake_pos[0], snake_pos[item]):
            game_over()
        snake_pos[item] = snake_pos[item-1]

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

    window.blit(text,(420,30))
    pygame.display.update()
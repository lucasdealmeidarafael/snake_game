from pygame.locals import *

class Config:
    # Windows
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    BLOCK_SIZE = 10
    STARTING_POS = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    #Colors
    COLORS = {
        'background': (0,0,0),
        'snake': (255,255,255),
        'apple': (255,0,0),
        'obstacle': (82,82,82),
        'text': (255,255,255)
    }

    # Game configurations
    INITIAL_VELOCITY = 10
    VELOCITY_INCREMENT = 2
    OBSTACLE_INTERVAL = 5
    DIRECTION_MAP = {
        K_UP: (0,-1),
        K_DOWN: (0,1),
        K_LEFT: (-1,0),
        K_RIGHT: (1,0)
    }

    
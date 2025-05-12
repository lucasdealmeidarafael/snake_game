from constants import Config
from pygame.locals import *

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [
            Config.STARTING_POS,
            (Config.STARTING_POS[0] + Config.BLOCK_SIZE, Config.STARTING_POS[1]),
            (Config.STARTING_POS[0] + 2 * Config.BLOCK_SIZE, Config.STARTING_POS[1])
        ]
        self.direction = K_LEFT

    def move(self):
        dx, dy = Config.DIRECTION_MAP[self.direction]
        new_head = (
        self.body[0][0] + dx * Config.BLOCK_SIZE,
        self.body[0][1] + dy * Config.BLOCK_SIZE
        )
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])


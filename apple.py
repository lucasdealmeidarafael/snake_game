import random 
from constants import Config

class Apple:
    def __init__(self, obstacles):
        self.position = self._generate_position(obstacles)

    @staticmethod
    def _generate_position(obstacles):
        while True:
            x = random.randint(0, Config.WINDOW_WIDTH - Config.BLOCK_SIZE)
            y = random.randint(0, Config.WINDOW_HEIGHT - Config.BLOCK_SIZE)
            position = (x // Config.BLOCK_SIZE * Config.BLOCK_SIZE,
                        y // Config.BLOCK_SIZE * Config.BLOCK_SIZE)
            
            if position not in obstacles:
                return position
            
            
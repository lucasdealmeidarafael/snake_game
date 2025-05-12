import pygame
import time
from constants import Config
from snake import Snake
from apple import Apple

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        pygame.display.set_caption('Sna Snake')
        self.font = pygame.font.SysFont('arial', 35, True, True)
        self.next_direction = None
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.obstacles = []
        self.points = 0
        self.velocity = Config.INITIAL_VELOCITY
        self.apple = Apple(self.obstacles)
        self.running = True

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._buffer_direction(event.key)

    def _buffer_direction(self, key):
        """Stores the valid direction to be used in the next move"""
        if key in Config.DIRECTION_MAP:
            current_dx, current_dy = Config.DIRECTION_MAP[self.snake.direction]
            new_dx, new_dy = Config.DIRECTION_MAP[key]
            
            # Check if it is not reverse motion
            if (current_dx + new_dx, current_dy + new_dy) != (0, 0):
                self.next_direction = key

    def _change_direction(self, key):
        if key in Config.DIRECTION_MAP:
            current_dx, current_dy = Config.DIRECTION_MAP[self.snake.direction]
            new_dx, new_dy = Config.DIRECTION_MAP[key]

            # Avoiding reverse movement
            if (current_dx + new_dx, current_dy + new_dy) != (0,0):
                self.snake.direction = key

    def _update_game_state(self):
        # Applies buffered direction
        if self.next_direction is not None:
            self.snake.direction = self.next_direction
            self.next_direction = None  # Reset the buffer
        
        self.snake.move()

        if self.snake.body[0] == self.apple.position:
            self._handle_apple_collision()

        self._check_collisions()

    def _handle_apple_collision(self):
        self.snake.grow()
        self.points += 1
        self.obstacles.append(Apple._generate_position(self.obstacles))
        self.apple = Apple(self.obstacles)

        if self.points % Config.OBSTACLE_INTERVAL == 0:
            self.velocity += Config.VELOCITY_INCREMENT

    def _check_collisions(self):
        head = self.snake.body[0]
        conditions = [
            self._is_out_of_bounds(head),
            head in self.snake.body[1:],
            head in self.obstacles
        ]

        if any(conditions):
            self._game_over()

    def _is_out_of_bounds(self, position):
        x, y = position
        return not (0 <= x < Config.WINDOW_WIDTH and 0 <= y < Config.WINDOW_HEIGHT)
    
    def _game_over(self):
        self._show_game_over_message()
        time.sleep(2)
        self.reset()

    def _show_game_over_message(self):
        font = pygame.font.SysFont('arial', 60, True, True)
        text = font.render('Game Over', True, Config.COLORS['text'])
        self.window.blit(text, (110, 300))

        pygame.display.update()

    def run(self):
        while self.running:
            pygame.time.Clock().tick(self.velocity)
            self._handle_input()
            self._update_game_state()
            self._draw()

    def _draw(self):
        self.window.fill(Config.COLORS['background'])

        # Draw elements
        self._draw_obstacles()
        self._draw_snake()
        self._draw_apple()
        self._draw_score()

        pygame.display.update()

    def _draw_obstacles(self):
        for obstacle in self.obstacles:
            pygame.draw.rect(self.window, Config.COLORS['obstacle'],
                             (*obstacle, Config.BLOCK_SIZE, Config.BLOCK_SIZE))
            
    def _draw_snake(self):
        for segment in self.snake.body:
            pygame.draw.rect(self.window, Config.COLORS['snake'],
                             (*segment, Config.BLOCK_SIZE, Config.BLOCK_SIZE))
            
    def _draw_apple(self):
        pygame.draw.rect(self.window, Config.COLORS['apple'],
                         (*self.apple.position, Config.BLOCK_SIZE, Config.BLOCK_SIZE))
        
    def _draw_score(self):
        text = self.font.render(f'Points: {self.points}', True, Config.COLORS['text'])
        self.window.blit(text, (420,30))
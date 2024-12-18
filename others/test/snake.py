import pygame
import sys
import time
import random

# Direction constants
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

class SnakeGame:
    def __init__(self, width=800, height=600, block_size=20):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = RIGHT
        self.food = self.set_new_food()
        self.score = 0
        self.speed = 10

        pygame.init()
        self.display = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Snake Game')
        self.font = pygame.font.Font(None, 36)

    def set_new_food(self):
        while True:
            x = random.randint(0, self.width - self.block_size) // self.block_size * self.block_size
            y = random.randint(0, self.height - self.block_size) // self.block_size * self.block_size
            food = (x, y)
            if food not in self.snake:
                return food

    def play(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT

            head = self.snake[-1]
            if self.direction == UP:
                new_head = (head[0], head[1] - self.block_size)
            elif self.direction == DOWN:
                new_head = (head[0], head[1] + self.block_size)
            elif self.direction == LEFT:
                new_head = (head[0] - self.block_size, head[1])
            elif self.direction == RIGHT:
                new_head = (head[0] + self.block_size, head[1])

            self.snake.append(new_head)
            if self.food == new_head:
                self.score += 1
                self.food = self.set_new_food()
            else:
                self.snake.pop(0)

            if (new_head[0] < 0 or new_head[0] >= self.width or
                    new_head[1] < 0 or new_head[1] >= self.height or
                    new_head in self.snake[:-1]):
                print("Game Over!")
                print("Final Score:", self.score)
                break

            self.display.fill((0, 0, 0))
            for pos in self.snake:
                pygame.draw.rect(self.display, (0, 255, 0), (pos[0], pos[1], self.block_size, self.block_size))
            pygame.draw.rect(self.display, (255, 0, 0), (self.food[0], self.food[1], self.block_size, self.block_size))
            text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.display.blit(text, (10, 10))
            pygame.display.update()
            clock.tick(self.speed)

if __name__ == "__main__":
    game = SnakeGame()
    game.play()

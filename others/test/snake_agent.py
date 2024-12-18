import gym
from gym import spaces
from gym.utils import play
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pygame
import sys
import random
import os

class SnakeEnvironment(gym.Env):
    def __init__(self, width=800, height=600, block_size=20):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 2
        self.food = self.set_new_food()
        self.score = 0

        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=255, shape=(self.height, self.width, 3), dtype=np.uint8)

    def set_new_food(self):
        while True:
            x = random.randint(0, self.width - self.block_size) // self.block_size * self.block_size
            y = random.randint(0, self.height - self.block_size) // self.block_size * self.block_size
            food = (x, y)
            if food not in self.snake:
                return food

    def reset(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = 2
        self.food = self.set_new_food()
        self.score = 0
        return self.get_observation()

    def step(self, action):
        reward = 0
        done = False

        if action == 0 and self.direction != 2:
            self.direction = 0
        elif action == 1 and self.direction != 3:
            self.direction = 1
        elif action == 2 and self.direction != 0:
            self.direction = 2
        elif action == 3 and self.direction != 1:
            self.direction = 3

        head = self.snake[-1]
        if self.direction == 0:
            new_head = (head[0], head[1] - self.block_size)
        elif self.direction == 1:
            new_head = (head[0] - self.block_size, head[1])
        elif self.direction == 2:
            new_head = (head[0] + self.block_size, head[1])
        elif self.direction == 3:
            new_head = (head[0], head[1] + self.block_size)

        self.snake.append(new_head)
        if self.food == new_head:
            self.score += 1
            self.food = self.set_new_food()
            reward = 1
        else:
            self.snake.pop(0)

        if (new_head[0] < 0 or new_head[0] >= self.width or
                new_head[1] < 0 or new_head[1] >= self.height or
                new_head in self.snake[:-1]):
            done = True
            reward = -1

        return self.get_observation(), reward, done, {}

    def get_observation(self):
        observation = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        for pos in self.snake:
            observation[pos[1] // self.block_size, pos[0] // self.block_size, :] = (0, 255, 0)
        observation[self.food[1] // self.block_size, self.food[0] // self.block_size, :] = (255, 0, 0)
        return observation

    def render(self, mode='human'):
        pygame.init()
        display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            display.fill((0, 0, 0))
            for pos in self.snake:
                pygame.draw.rect(display, (0, 255, 0), (pos[0], pos[1], self.block_size, self.block_size))
            pygame.draw.rect(display, (255, 0, 0), (self.food[0], self.food[1], self.block_size, self.block_size))
            pygame.display.update()
            clock.tick(60)
        pygame.quit()

class DeepQAgent:
    def __init__(self, env):
        self.env = env
        self.model = keras.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(env.height, env.width, 3)),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(env.action_space.n)
        ])
        self.model.compile(optimizer='adam', loss='mse')
        self.best_reward = -np.inf

    def train(self, episodes=1000):
        for episode in range(episodes):
            state = self.env.reset()
            done = False
            rewards = 0
            while not done:
                action = np.argmax(self.model.predict(state[np.newaxis, :]))
                state, reward, done, _ = self.env.step(action)
                rewards += reward
            if rewards > self.best_reward:
                self.best_reward = rewards
                self.model.save('best_model.h5')
            print(f'Episode {episode+1}, Reward: {rewards}')

    def test(self):
        state = self.env.reset()
        done = False
        rewards = 0
        while not done:
            action = np.argmax(self.model.predict(state[np.newaxis, :]))
            state, reward, done, _ = self.env.step(action)
            rewards += reward
            self.env.render()
        print(f'Reward: {rewards}')

env = SnakeEnvironment()
agent = DeepQAgent(env)
agent.train()
agent.test()

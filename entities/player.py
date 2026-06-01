import pygame
from core.settings import PLAYER_SIZE, PLAYER_SPEED

class Player:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = PLAYER_SIZE
        self.speed = PLAYER_SPEED
        self.holding_food = None

    def move(self, keys, up, down, left, right):
        if keys[up]:
            self.y -= self.speed
        if keys[down]:
            self.y += self.speed
        if keys[left]:
            self.x -= self.speed
        if keys[right]:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            (self.x, self.y, self.size, self.size)
        )
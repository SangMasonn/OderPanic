import pygame
import random

foods = [
    "Burger",
    "Pizza",
    "Fries",
    "Hotdog"
]

class Customer:

    def __init__(self, table):
        self.table = table
        self.food = random.choice(foods)
        self.wait_time = 600
        self.finished = False
        self.order_taken = False

    def update(self):
        if not self.finished:
            self.wait_time -= 1

    def draw(self, screen, font):
        x = self.table.rect.x
        y = self.table.rect.y

        color = (255, 220, 0)

        if self.order_taken:
            color = (0, 255, 0)

        pygame.draw.circle(
            screen,
            color,
            (x + 120, y + 40),
            25
        )

        order_text = font.render(
            self.food,
            True,
            (255, 255, 255)
        )

        screen.blit(order_text, (x + 10, y - 30))

        time_text = font.render(
            str(self.wait_time // 60),
            True,
            (255, 100, 100)
        )

        screen.blit(time_text, (x + 110, y - 30))
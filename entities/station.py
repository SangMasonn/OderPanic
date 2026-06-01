import pygame

class Station:

    def __init__(self, x, y, w, h, name, color):

        self.rect = pygame.Rect(x, y, w, h)
        self.name = name
        self.color = color

    def draw(self, screen, font):

        pygame.draw.rect(screen, self.color, self.rect)

        text = font.render(self.name, True, (255, 255, 255))
        screen.blit(text, (self.rect.x + 10, self.rect.y + 10))
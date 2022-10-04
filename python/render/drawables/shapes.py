from python.render.drawables import drawable
import pygame

# This module implements all non-interactive primitive drawables


class Rectangle(drawable.Drawable):
    def __init__(self, color, pos, dim):
        super().__init__()
        self.color = color
        self.shape = pygame.Rect(pos, dim)

    def render(self):
        pygame.draw.rect(super().surface, self.color, self.shape)


class Circle(drawable.Drawable):
    def __init__(self):
        super().__init__()

    def render(self):
        pass

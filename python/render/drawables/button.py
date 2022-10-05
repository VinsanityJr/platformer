from python.render.drawables import drawable
import pygame


# This module implements the button, a drawable that can be pressed


class Button(drawable.Drawable):
    def __init__(self, color, pos, dim, on_click):
        super().__init__()

        # set the color, position, and dimension values
        self.color = color
        self.pos = pos
        self.dim = dim

        # save the shape of the button
        self.shape = pygame.Rect(pos, dim)

        # save the function to be triggered when clicked
        self.on_click = on_click

    # if the button is clicked, what should it do?
    def click(self, mousepos):
        # find a way to pass a function in as a variable.
        # Do something function-pointer-y
        if self.pos[0] <= mousepos[0] <= self.pos[0] + self.dim[0] and \
                self.pos[1] <= mousepos[1] <= self.pos[1] + self.dim[1]:

            # execute the button's function
            return self.on_click()

    def render(self):
        pygame.draw.rect(super().surface, self.color, self.shape)

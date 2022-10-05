from python.render.drawables import drawable
from python.util import settings

# This module implements a textbox drawable that can be used to add
# text to a screen


class Textbox(drawable.Drawable):
    def __init__(self, color, pos, text, font=None):
        super().__init__()

        # initialize the drawable's values
        self.pos = pos
        self.color = color
        self.text = text
        self.font = font

    def render(self):
        if self.font is not None:
            super().surface.blit(self.font.render(self.text, False, self.color), self.pos)
        else:
            super().surface.blit(settings.default_font.render(self.text, False, self.color), self.pos)

from python.render.drawables import drawable

# This module implements sprites. Sprites need to have various
# hitboxes and be able to contain various textures.


class sprite(drawable.Drawable):
    def __init__(self, texture):
        super().__init__()
        self.texture = texture

    def render(self):
        pass

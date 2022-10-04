from python.render.drawables import drawable
# This module implements the button, a drawable that can be pressed


class Button(drawable.Drawable):
    def __init__(self):
        super().__init__()

    # if the button is clicked, what should it do?
    def click(self):
        # find a way to pass a function in as a variable.
        # Do something function-pointer-y
        pass

    def render(self):
        pass

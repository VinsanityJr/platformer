from python.render import screen
from python.render.drawables import shapes

# This module contains the main menu class. This class contains the screen
# that contains all of the drawables as well as any other code that might
# be required for the main menu.


class Main_Menu(screen.Screen):
    def __init__(self):
        super().__init__()

        # add all the drawables for the main menu
        super().add_drawable(shapes.Rectangle((20, 20, 200), (100, 100), (50, 50)))

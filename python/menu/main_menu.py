from python.render import screen
from python.render.drawables import shapes
from python.render.drawables import textbox

# This module contains the main menu class. This class contains the screen
# that contains all the drawables as well as any other code that might be
# # required for the main menu.


class Main_Menu(screen.Screen):
    def __init__(self):
        super().__init__()

        # add all the drawables for the main menu
        super().add_drawable(shapes.Rectangle((20, 20, 200), (100, 100), (50, 50)))
        super().add_drawable(shapes.Rectangle((20, 20, 200), (160, 160), (50, 50)))
        super().add_drawable(textbox.Textbox((200, 100), (100, 10, 150), "Welcome to our game!"))
        super().add_drawable(textbox.Textbox((300, 250), (100, 10, 200), "It's a pretty cool game."))

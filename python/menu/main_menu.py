from python.render import screen
from python.render.drawables import shapes
from python.render.drawables import textbox
from python.util import colors

# This module contains the main menu class. This class contains the screen
# that contains all the drawables as well as any other code that might be
# # required for the main menu.


class Main_Menu(screen.Screen):
    def __init__(self):
        super().__init__()

        # add all the drawables for the main menu
        super().add_drawable(shapes.Rectangle(colors.BLACK, (100, 100), (50, 50)))
        super().add_drawable(shapes.Rectangle(colors.BLACK, (160, 160), (50, 50)))
        super().add_drawable(textbox.Textbox((200, 100), colors.BLACK, "Welcome to our game!"))
        super().add_drawable(textbox.Textbox((300, 250), colors.BLACK, "It's a pretty cool game."))
        super().add_drawable(textbox.Textbox((280, 470), colors.BLACK, "You should play it"))

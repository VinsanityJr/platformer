from python.render import screen
from python.render.drawables import shapes
from python.render.drawables import textbox
from python.render.drawables import button
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
        super().add_drawable(textbox.Textbox(colors.BLACK, (200, 100), "Welcome to our game!"))
        super().add_drawable(textbox.Textbox(colors.BLACK, (300, 250), "It's a pretty cool game."))
        super().add_drawable(textbox.Textbox(colors.BLACK, (280, 470), "You should play it"))
        super().add_drawable(button.Button(colors.BLACK, (10, 200), (30, 30), self.play))

    def play(self):
        print("Time to play the game!")

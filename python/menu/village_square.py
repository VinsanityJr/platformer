from python.menu import screens
from python.render import screen
from python.render.drawables import button
from python.util import colors
from python.util import settings


# This module contains the village square class. This class contains all the drawables
# and variables that are needed for the village square screen.


class Village_Square(screen.Screen):
    def __init__(self):
        super().__init__()

        # add all the drawables for the main menu
        super().add_drawable(button.Button(colors.BLACK, (200, 10), (30, 30), self.to_main_menu))

    def to_main_menu(self):
        settings.screen = screens.main_menu_screen

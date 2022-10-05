from python.util import settings
from python.util import colors
from python.util import event_helper as ev
from python.render.drawables import drawable
from python.menu import screens
import pygame

# the main file needs to handle window creation and gamestate management.
# This file needs to ensure that all communication between the user and
# the game and inter-game communications have a means of occurring.

# initialize pygame and its text engine
pygame.init()
settings.default_font = pygame.font.SysFont('Comic Sans MS', 30)  # freetype is apparently better than font

# open a blank surface
surface = pygame.display.set_mode(settings.SURFACE_SIZE)
surface.fill(colors.WHITE)  # eventually remove this

# set the surface that everything is going to be drawn to.
drawable.Drawable.surface = surface

# set the default screen to the main menu
settings.screen = screens.main_menu_screen

# main loop
while not settings.exit_program:
    # pet the event helper
    ev.pet_event_helper()

    if settings.gamestate == "menu":
        settings.screen.render()

    settings.screen.on_click(ev.get_mouse_pos())

    # blit the new things to the screen
    pygame.display.flip()

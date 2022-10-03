from python.util import settings
from python.util import event_helper as ev
import pygame

# the main file needs to handle window creation and gamestate management.
# This file needs to ensure that all communication between the user and
# the game and inter-game communications have a means of occurring.

# initialize pygame
pygame.init()

# open a blank screen
screen = pygame.display.set_mode(settings.SCREEN_SIZE)
screen.fill((255, 255, 255))

# audio logic

# main render loop
while not settings.exit_program:
    # pet the event helper
    ev.pet_event_helper()

    # blit the new things to the screen
    pygame.display.flip()

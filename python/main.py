from python.util import settings
import pygame

# the main file needs to handle window creation and gamestate management.
# This file needs to ensure that all communication between the user and
# the game and inter-game communications have a means of occurring.

# Quick access to basic keys that will be used
from pygame.locals import(
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# initialize pygame
pygame.init()

# open a blank screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
screen.fill((255, 255, 255))

# audio logic

# main render loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # blit the new things to the screen
    pygame.display.flip()

import pygame

#Quick access to basic keys that will be used
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# the main loop needs to handle window creation and gamestate.
pygame.init()

# open a window here
    #Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

    #Create screen object and fill it with white background
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255,255,255))


# audio logic

# main render loop (I'll help here)
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    pygame.display.flip()

# I'm not sure how to handle user input yet, but that's a later issue

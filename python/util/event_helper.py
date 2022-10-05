from python.util import settings
import pygame

# The event helper does two things: it keeps track of which events
# have been pressed, and it allows an object to query if a given key
# has been pressed.

# key abbreviations
ESCAPE = pygame.K_ESCAPE
A = pygame.K_a
D = pygame.K_d
S = pygame.K_s
W = pygame.K_w

# A dictionary of all the keys to poll for
key_events = {
    ESCAPE: "",
    A: "",
    D: "",
    S: "",
    W: ""
}


# pet the event helper! When pet, the event helper will update all of
# its key input data
def pet_event_helper():
    # delete the entries from the last time the event helper was pet
    clear_event_helper()

    # iterate through the events
    for event in pygame.event.get():
        # get keydown events
        if event.type == pygame.KEYDOWN:
            if event.key in key_events:
                key_events[event.key] = "down"

        # get keyup events
        elif event.type == pygame.KEYUP:
            if event.key in key_events:
                key_events[event.key] = "up"

        # if the user hit the 'x' button, exit the program
        elif event.type == pygame.QUIT:
            settings.exit_program = True

    # if the escape key was pressed, exit the program
    if key_events[ESCAPE] != "":
        settings.exit_program = True


# clear all keys in the event dictionary
def clear_event_helper():
    for key in key_events:
        key_events[key] = ""


# poll the dictionary for a given key
def get_key_state(key):
    return key_events[key]


# ask pygame what the current mouse position is
def get_mouse_pos():
    return pygame.mouse.get_pos()

import pygame

# The event helper does two things: it keeps track of which events
# have been pressed, and it allows an object to query if a given key
# has been pressed.

# A list of the event types to poll for
events_of_interest = [
    pygame.key.xxx
]

# if event in events_of_interest, add it to a list of boolean values.
# maybe use a dictionary of event types and whether it is true or false?

# Then write code to poll the dictionary
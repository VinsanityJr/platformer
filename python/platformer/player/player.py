# The player is the character that the user is playing as. Most
# interactions between the user and the level are done through the
# player object.

class Player:
    def __init__(self):
        self.pos = (0, 0)
        self.velocity = (0, 0)
        self.acceleration = (0, 0)

# The level object is the target of most of the interactions that the
# player will make while inside the platformer. It contains the tiles
# in the current level, the player object, and any other elements of
# gameplay.

class Level:
    def __init__(self, level):
        self.level = level

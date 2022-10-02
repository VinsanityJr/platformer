# tiles are the base unit of level design.

# TileType class
class TileType:
    def __init__(self, name):
        self.name = name


# Tile class
class Tile:
    def __init__(self, tile_type):
        self.tile_type = tile_type

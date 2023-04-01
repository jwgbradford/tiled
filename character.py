import pygame as pg
from const import BLACK, TRANSPARENT, TILE_SIZE, TILES_VERTICAL, TILES_HORIZONTAL

COLUMN = TILES_HORIZONTAL / 2
ROW = TILES_HORIZONTAL / 2
POS = (COLUMN, ROW)

class Character:
    def __init__(self, colour = BLACK, pos = POS) -> None:
        self.column, self.row = pos
        self.costume = self.make_character_image(colour)

    def make_character_image(self, colour):
        # simple player costume
        tile = pg.Surface((TILE_SIZE, TILE_SIZE))
        tile.fill(TRANSPARENT)
        # set black as transparent
        tile.set_colorkey(TRANSPARENT)
        # draw a circle for our player in the middle of the tile
        MID_TILE = TILE_SIZE / 2
        pg.draw.circle(tile, colour, (MID_TILE, MID_TILE), MID_TILE / 2)
        return tile
    
    def get_costume(self):
        return self.costume

    def get_pos(self):
        return (self.column * TILE_SIZE, self.row * TILE_SIZE)
    
    def get_tile(self):
        return (self.column, self.row)

    def set_tile(self, tile):
        self.column = tile[0]
        self.row = tile[1]

    def update(self) -> None:
        pass
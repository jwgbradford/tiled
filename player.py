import pygame as pg
from const import BLACK, D_RED, TILE_SIZE, TILES_HORIZONTAL, TILES_VERTICAL

class Player:
    def __init__(self) -> None:
        self.column, self.row = (1, 2)
        self.costume = self.make_player_image()

    def make_player_image(self):
        # simple player costume
        tile = pg.Surface((TILE_SIZE, TILE_SIZE))
        tile.fill(BLACK)
        # set black as transparent
        tile.set_colorkey(BLACK)
        # draw a circle for our player in the middle of the tile
        MID_TILE = TILE_SIZE / 2
        pg.draw.circle(tile, D_RED, (MID_TILE, MID_TILE), MID_TILE / 2)
        return tile
    
    def pos(self):
        return (self.column * TILE_SIZE, self.row * TILE_SIZE)
    
    def update(self, key_pressed) -> None:
        if key_pressed == pg.K_UP:
            self.row -= 1
            if self.row < 0:
                self.row = 0
        elif key_pressed == pg.K_DOWN:
            self.row += 1
            if self.row == TILES_VERTICAL:
                self.row -= 1
        elif key_pressed == pg.K_LEFT:
            self.column -= 1
            if self.column < 0:
                self.column = 0
        elif key_pressed == pg.K_RIGHT:
            self.column +=1
            if self.column == TILES_VERTICAL:
                self.column -= 1
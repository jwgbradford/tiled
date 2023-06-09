import pygame as pg
from character import Character
from const import D_RED, TILES_VERTICAL, TILES_HORIZONTAL

class Player(Character):
    def __init__(self) -> None:
        colour = D_RED
        pos = (1, 2)
        super().__init__(colour, pos)

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
            if self.column == TILES_HORIZONTAL:
                self.column -= 1
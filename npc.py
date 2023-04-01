import pygame as pg
from character import Character
from const import MAGENTA, TILES_VERTICAL, TILES_HORIZONTAL
from random import randint

class Npc(Character):
    def __init__(self, map, pos = (1, 1), colour = MAGENTA) -> None:
        super().__init__(colour, pos)
        self.map = map

    def get_map(self):
        return self.map

    def update(self) -> None:
        move_choice = randint(1, 8)
        if move_choice == 1:
            self.row -= 1
            if self.row < 0:
                self.row = 0
        elif move_choice == 3:
            self.row += 1
            if self.row == TILES_VERTICAL:
                self.row -= 1
        elif move_choice == 5:
            self.column -= 1
            if self.column < 0:
                self.column = 0
        elif move_choice == 7:
            self.column +=1
            if self.column == TILES_HORIZONTAL:
                self.column -= 1
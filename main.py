import pygame as pg
import sys
from const import TILES_HORIZONTAL, TILES_VERTICAL, TILE_SIZE, COLOUR_LIST
from maps import MAP1
from player import Player
from renderer import Renderer

class MyGame:
    def __init__(self) -> None:
        self.my_screen = Renderer()
        self.player = Player()
        self.my_screen.make_background_map(MAP1)

    def run(self) -> None:
        self.my_screen.update_graphics(self.player.costume, self.player.pos)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    self.events_update(event)
                    self.my_screen.update_graphics(self.player.costume, self.player.pos)

    def events_update(self, event) -> None:
            self.player.update(event.key)


if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()
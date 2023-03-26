import pygame as pg
import sys
from maps import MAPS
from player import Player
from renderer import Renderer

class MyGame:
    def __init__(self) -> None:
        self.my_screen = Renderer()
        self.player = Player()
        self.player.set_tile((4, 4))
        self.current_map = list(MAPS.keys())[0]
        self.my_screen.make_background_map(MAPS[self.current_map]['map'])

    def run(self) -> None:
        self.my_screen.update_graphics(self.player.costume, self.player.get_pos)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    self.events_update(event)
                    self.map_update()
                    self.my_screen.update_graphics(self.player.costume, self.player.get_pos)

    def events_update(self, event) -> None:
        self.player.update(event.key)

    def map_update(self) -> None:
        new_location = self.current_map
        for location in MAPS[self.current_map]['locations']:
            if self.player.get_tile() == location[0]:
                new_location = location[1]
                self.my_screen.make_background_map(MAPS[new_location]['map'])
                self.player.set_tile((4, 4))
                break
        self.current_map = new_location

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()
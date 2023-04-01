import pygame as pg
import sys
from maps import MAPS
from player import Player
from renderer import Renderer
from npc import Npc
from const import PURPLE

class MyGame:
    def __init__(self) -> None:
        self.my_screen = Renderer()
        # create player and set starting tile
        self.player = Player()
        self.npcs = []
        self.npcs.append(Npc('town_1', (2, 4), PURPLE))
        self.player.set_tile((4, 4))
        # set starting map as first map in dictionary
        self.current_map = list(MAPS.keys())[0]
        self.my_screen.make_background_map(MAPS[self.current_map]['map'])

    def run(self) -> None:
        # first screen update
        self.my_screen.update_graphics(self.player, self.current_map, self.npcs)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    self.events_update(event)
                    self.npc_update()
                    self.map_update()
                    # only update the screen if there's a key press
                    self.my_screen.update_graphics(self.player, self.current_map, self.npcs)

    def events_update(self, event) -> None:
        self.player.update(event.key)

    def npc_update(self) -> None:
        for npc in self.npcs:
            npc.update()
    
    def map_update(self) -> None:
        # snapshot of current location
        new_location = self.current_map
        for location in MAPS[self.current_map]['locations']:
            if self.player.get_tile() == location[0]:
                # set new location
                new_location = location[1]
                # set new map background image
                self.my_screen.make_background_map(MAPS[new_location]['map'])
                # reset player a centre of screen
                self.player.set_tile((4, 4))
                break
        self.current_map = new_location

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()
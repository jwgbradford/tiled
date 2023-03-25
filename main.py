import pygame as pg
import sys
from const import TILES_HORIZONTAL, TILES_VERTICAL, TILE_SIZE, COLOUR_LIST
from maps import MAP1
from player import Player

WORLD_WIDTH = TILES_HORIZONTAL * TILE_SIZE
WORLD_HEIGHT = TILES_VERTICAL * TILE_SIZE

class MyGame:
    def __init__(self) -> None:
        pg.init()
        self.game_window = pg.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))
        self.background = self.make_background()
        self.player = Player()

    def run(self) -> None:
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    self.player.update(event.key)
            self.game_window.blit(self.background, (0,0))
            self.game_window.blit(self.player.costume, (self.player.pos()))
            pg.display.update()

    def make_background(self): # this function creates a single image background
        # create a temporary surface
        tile = pg.Surface((TILE_SIZE - 1, TILE_SIZE - 1))
        # create our main background surface
        background = pg.Surface((WORLD_WIDTH, WORLD_HEIGHT))
        # make sure it's black (t show grid lines)
        background.fill(COLOUR_LIST[13])
        # Use two nested for loops to get the coordinates.
        for column in range(TILES_HORIZONTAL):
            for row in range(TILES_VERTICAL):
                # pick the colour values from the map
                colour_value = MAP1[column][row]
                # convert to (r, g, b) using our colour list
                rgb = COLOUR_LIST[colour_value]
                # fill in each background tile
                tile.fill(rgb)
                # blit the tile at its respective coords
                background.blit(
                    tile, 
                    ((row * TILE_SIZE), (column * TILE_SIZE))
                    )
        #returns a surface, ready to be sent to the screen
        return background

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()
import pygame as pg
from const import TILES_HORIZONTAL, TILES_VERTICAL, TILE_SIZE, WORLD_WIDTH, WORLD_HEIGHT, COLOUR_LIST

class Renderer:
    def __init__(self) -> None:
        pg.init()
        self.game_window = pg.display.set_mode((WORLD_WIDTH, WORLD_HEIGHT))

    def make_background_map(self, MAP) -> None: # this function creates a single image background
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
                colour_value = MAP[column][row]
                # convert to (r, g, b) using our colour list
                rgb = COLOUR_LIST[colour_value]
                # fill in each background tile
                tile.fill(rgb)
                # blit the tile at its respective coords
                background.blit(
                    tile, 
                    ((row * TILE_SIZE), (column * TILE_SIZE))
                    )
        #set a surface, ready to be sent to the screen
        self.background_map = background

    def update_graphics(self, player, map, npc_list) -> None:
            self.game_window.blit(self.background_map, (0,0))
            # get our costume & position for the player
            player_image = player.get_costume()
            player_pos = player.get_pos()
            self.game_window.blit(player_image, player_pos)
            for npc in npc_list:
                if npc.get_map() == map:
                    # get our costume & position for the npc
                    npc_image = npc.get_costume()
                    npc_pos = npc.get_pos()
                    self.game_window.blit(npc_image, npc_pos)            
            pg.display.update()
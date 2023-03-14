import numpy as np
WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32
FPS = 60
SPEED = 3

GRASS_LAYER = 1
BLOCK_LAYER =2
PLAYER_LAYER = 3
MONSTER_LAYER = 4

RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)



# def loadMap():
#     # with open("img/tilemaps/basic.csv") as f:
#     #     for line in f:
#     #         print(line.strip())
#     csvData = open('img/tilemaps/basic.csv')
#     tilemap = np.loadtxt(csvData,delimiter=",")
#     return tilemap
        
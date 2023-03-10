import pygame
import numpy as np
import sys
from sprites import *
from config import *
from map import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font('Arial',32)
        self.running = True
        self.tilemap = self.loadMap()
        pygame.display.set_caption("RPGPY")
    
    
    def new(self):
        # a new game starts
        self.playing = True
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.map = pygame.sprite.LayeredUpdates()
        

        # self.map = Map(self,self.tilemap)
        self.createTilemap()
        
    def createTilemap(self):
        for j in range(len(self.tilemap)):

            for i in range(len(self.tilemap[j])):
                if self.tilemap[j][i] == 1:
                    Grass(self,i,j)
                    Block(self,i,j)
                if self.tilemap[j][i] == 0:
                    Grass(self,i,j)
                    self.player = Player(self,i,j)
                if self.tilemap[j][i] == -1:
                    Grass(self,i,j)
        
        
    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            
            
        
    def update(self):
        #game loop updates
        self.all_sprites.update()
        # print(self.tilemap)
       
    
    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
        
    def game_over(self):
        pass
    def intro_screen(self):
        pass
    def loadMap(self):
        # with open("img/tilemaps/basic.csv") as f:
        #     for line in f:
        #         print(line.strip())
        csvData = open('img/tilemaps/basic.csv')
        tilemap = np.loadtxt(csvData,delimiter=",")
        return tilemap


gameInstance= Game()
gameInstance.intro_screen()
gameInstance.new()
while gameInstance.running:
    gameInstance.main()
    gameInstance.game_over()
pygame.quit()
sys.exit()


# pygame.init()
# screen = pygame.display.set_mode((500,500))
# gameloop = True
# pygame.display.set_caption("RPGPY: Ben Ashby")
# clock = pygame.time.Clock()

# while gameloop:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
    
    
#     pygame.display.flip()
#     clock.tick(60)
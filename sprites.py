import pygame
from config import *
import math
import time
import random



class Player(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.facing = 'down'
        
        image_to_load = pygame.image.load("img/Character_back.png")
        
        self.image = pygame.Surface([self.width,self.height])
        self.image.blit(image_to_load,(0,0))
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y = round(self.x/32)
            x = round(self.y/32)-1
            if self.game.tilemap[x][y] == 1:
                print(f"collision at ({x},{y})")
                pass
            else:
                self.y -=SPEED
                self.facing = 'up'
                image_to_load = pygame.image.load("img/Character_forward.png")
            
                self.image = pygame.Surface([self.width,self.height])
                self.image.blit(image_to_load,(0,0))
                self.image.set_colorkey(WHITE)
            
        if keys[pygame.K_s]:
            y = round(self.x/32)
            x = round(self.y/32)+1
            if self.game.tilemap[x][y] == 1:
                print(f"collision at ({x},{y})")
                pass
            else:
                self.y +=SPEED
                self.facing = 'down'
                image_to_load = pygame.image.load("img/Character_back.png")
            
                self.image = pygame.Surface([self.width,self.height])
                self.image.blit(image_to_load,(0,0))
                self.image.set_colorkey(WHITE)
        if keys[pygame.K_a]:
            y= round(self.x/32) -1
            x = round(self.y/32)
            if self.game.tilemap[x][y] == 1:
                print(f"collision at ({x},{y})")
                pass
            else:
                self.x -=SPEED
                self.facing = 'left'
                image_to_load = pygame.image.load("img/Character_left.png")
            
                self.image = pygame.Surface([self.width,self.height])
                self.image.blit(image_to_load,(0,0))
                self.image.set_colorkey(WHITE)
        if keys[pygame.K_d]:
        
            y= round(self.x/32) + 1
            
            x = round(self.y/32)

            if self.game.tilemap[x][y] == 1:
                print(f"collision at ({x},{y})")
                pass
            else:   
                self.x +=SPEED
                print(x)
                self.facing = 'right'
                image_to_load = pygame.image.load("img/Character_right.png")
            
                self.image = pygame.Surface([self.width,self.height])
                self.image.blit(image_to_load,(0,0))
                self.image.set_colorkey(WHITE)
        if keys[pygame.K_e]:
            if self.facing == 'right':
                # temp_x = self.x +1
                # image_to_load = pygame.image.load("img/slash.png")
                
                # self.slashImage = pygame.Surface((self.width,self.height))
                # self.slashImage.blit(image_to_load, (0,0))
                # self.slashImage.set_colorkey(WHITE)
                
                Attack(self.game,self.x+32,self.y, self)
            if self.facing == 'left':
                Attack(self.game,self.x-32,self.y,self)
            if self.facing == 'up':
                Attack(self.game,self.x,self.y-32,self) 
            if self.facing == 'down':
                Attack(self.game,self.x,self.y+32,self)
                
                

class Block(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        image_to_load = pygame.image.load("img/rock.png")
        
        self.image = pygame.Surface([self.width,self.height])
        self.image.blit(image_to_load,(0,0))
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        
        
    def update(self):
        pass

class Grass(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._layer = GRASS_LAYER
        self.groups = self.game.all_sprites, self.game.map
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x * TILESIZE
        self.y = y *TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        image_to_load = pygame.image.load("img/grass.png")
        
        self.image = pygame.Surface([self.width,self.height])
        self.image.blit(image_to_load,(0,0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        
    def update(self):
        pass
class Attack(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y, player):
        self.game = game
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        self.player = player
        
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        image_to_load =  pygame.image.load("img/slash.png")
        
        self.image = pygame.Surface([self.width,self.height])
        self.image.blit(image_to_load, (0,0))
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.loop = 0
        self.active = False
        
    def update(self):
        self.collide()
        print("update loop")
    def collide(self):
        
        direction = self.player.facing
        
        
        if direction == 'right':
            self.loop  += 0.5
            print(self.loop)
            
            if self.loop >= 5:
                self.kill()
                self.loop = 0
        if direction == 'left':
            self.loop  += 0.5
            print(self.loop)
            
            if self.loop >= 5:
                self.kill()
                self.loop = 0
        if direction == 'up':
            self.loop  += 0.5
            print(self.loop)
            
            if self.loop >= 5:
                self.kill()
                self.loop = 0
        if direction == 'down':
            self.loop  += 0.5
            print(self.loop)
            
            if self.loop >= 5:
                self.kill()
                self.loop = 0                
                
        
        
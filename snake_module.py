import pygame
import os
import sys
import random
import time

SCREEN_WIDTH = 1200 #800/20=40
SCREEN_HEIGHT = 900 #600/20=30

GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT/GRID_SIZE

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

WHITE = (255,255,255)
ORANGE = (250,150,0)
GRAY = (100,100,100)

class Snake():
    def __init__(self):
        self.create()

    def create(self):
        self.length = 2
        self.positions = [(int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def control(self,xy):
        if (xy[0]*-1, xy[1]*-1) == self.direction: # 반대방향 금지: up(0,-1),dn(0,1);r(1,0),l(-1,0)
            return
        else:
            self.direction = xy

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (cur[0] + (x*GRID_SIZE)), (cur[1] + (y*GRID_SIZE))
        if new in self.positions[2:]: # 자기 몸 물기
            time.sleep(1)
            self.create()
        elif (new[0] < 0 or new[0] > SCREEN_WIDTH) or (new[1] < 0 or new[1] > SCREEN_HEIGHT): # 경계이탈
            time.sleep(1)
            self.create()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def eat(self):
        self.length += 1

    def draw(self,screen):
         red, green, blue = 255/(self.length-1),95,7/(self.length-1)
         for i, p in enumerate(self.positions):
            color = (red, green, blue)
            # color = (int((255/self.length)*i)
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen,color,rect)
            pygame.draw.rect(screen, color, [p[0],p[1],GRID_SIZE,GRID_SIZE])

class Feed():
    def __init__(self):
        self.position = (0,0)
        self.color = ORANGE
        self.create()

    def create(self):
        x = random.randint(0, GRID_WIDTH-1)
        y = random.randint(0, GRID_HEIGHT-1)
        self.position = x*GRID_SIZE, y*GRID_SIZE
        

    def draw(self, screen):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, self.color, rect)

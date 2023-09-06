import pygame
import os
import sys
import random
import time
from snake_module import Snake, Feed
from pygame import mixer
mixer.init()
mixer.music.load('bg_music_1.mp3')
mixer.music.play(-1)

feed_sound = mixer.Sound('eat_sound.wav')

SCREEN_WIDTH = 1200 # 800/20=40
SCREEN_HEIGHT = 900 # 600/20=30

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

class Game():
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.speed = 5

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.control(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.control(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.control(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.control(RIGHT)

        return False

    def run_logic(self):
        self.snake.move()
        self.check_eat(self.snake, self.feed)
        self.speed = (10 + self.snake.length) / 2

    def check_eat(self, snake, feed):
        if snake.positions[0] == feed.position:
            feed_sound.play()
            snake.eat()
            feed.create()

    def draw_info(self, length, speed, screen):
        info = "Length: " + str(length) + "   " + "Speed: " + str(round(speed,2))
        font = pygame.font.SysFont('FixedSys', 30, False, False)
        text_obj = font.render(info, True, GRAY)
        text_rect = text_obj.get_rect()
        text_rect.x, text_rect.y = 10, 10
        screen.blit(text_obj, text_rect)

    def display_frame(self, screen):
        screen.fill(WHITE)
        self.draw_info(self.snake.length, self.speed, screen)
        self.snake.draw(screen)
        self.feed.draw(screen)
        screen.blit(screen, (0,0))

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)

        pygame.display.flip()
        clock.tick(game.speed)

    pygame.quit()
import pygame
import random

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

WHITE = (255,255,255)
SEA = (80,180,220)
GROUND = (140,120,40)
DARK_GROUND = (70,60,20)

FPS = 60

class Fish():
    def __init__(self):
        self.image = pygame.image.load('fish.png')
        self.sound = pygame.mixer.Sound('swim.wav')
        self.rect = self.image.get_rect()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height
        self.reset()

    def reset(self):
        self.rect.x = 250
        self.rect.y = 250
        self.dx = 0
        self.dy = 0

    def swim(self):
        self.dy = -10
        self.sound.play()

    def update(self):
        self.dy += 0.5
        self.rect.y += self.dy

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y + self.height > SCREEN_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - self.height
            self.dy = 0

        if self.dy > 20:
            self.dy = 20

    def draw(self,screen):
        screen.blit(self.image,self.rect)

pygame.init()
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play(-1)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

fish = Fish()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fish.swim()

    screen.fill(SEA)
    fish.update()
    fish.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
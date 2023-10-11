import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

WHITE = (255,255,255)
BLUE = (20,60,120)
BLACK = (0,0,0)
RED = (255,0,0)

FPS = 60

class Ball():
    def __init__(self):
        self.rect = pygame.Rect(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2), 12, 12)
        self.dx = 7
        self.dy = 7
        self.bounce_sound = pygame.mixer.Sound('bounce.wav')

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0:
            self.dx *= -1
            self.rect.left = 0
            self.bounce_sound.play()
        elif self.rect.right > SCREEN_WIDTH:
            self.dx *= -1
            self.rect.right = SCREEN_WIDTH
            self.bounce_sound.play()
        if self.rect.top < 0:
            self.dy *= -1
            self.rect.top = 0
            self.bounce_sound.play()
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.dy *= -1
            self.rect.bottom = SCREEN_HEIGHT
            self.bounce_sound.play()

    def draw(self,screen):
        pygame.draw.rect(screen,WHITE,self.rect)

class Racket:
    def __init__ (self):
        self.rect = pygame.Rect(int(SCREEN_WIDTH)-25,SCREEN_HEIGHT-15,50,12)
        self.dx = 0
        self.ping_sound = pygame.mixer.Sound('ping.wav')

    def update(self,ball):
        if self.rect.left <= 0 and self.dx <0:
            self.dx = 0
        elif self.rect.right >= SCREEN_WIDTH and self.dx>0:
            self.dx= 0

        self.rect.x += self.dx

        if self.rect.colliderect(ball.rect):
            ball.dy *= -1
            ball.rect.bottom = self.rect.top
            self.ping_sound.play()

    def draw(self,screen):
        pygame.draw.rect(screen,RED,self.rect)

class Enemy:
    def __init__ (self):
        self.rect = pygame.Rect(int(SCREEN_WIDTH/2)-25,3,50,12)
        self.dx = 0
        self.pong_sound = pygame.mixer.Sound('pong.wav')

    def update(self,ball):
        diff_y = self.rect.bottom - ball.rect.top
        if diff_y < 200 and ball.dy < 0:
            if self.rect.center > ball.rect.center:
                self.dx = -5
            elif self.rect.center < ball.rect.center:
                self.dx = 5

        self.rect.x += self.dx

        if self.rect.colliderect(ball.rect):
            ball.dy *=  -1
            ball.rect.top = self.rect.bottom
            self.pong_sound.play()

    def draw(self,screen):
        pygame.draw.rect(screen,BLACK,self.rect)


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

ball = Ball()
racket = Racket()
enemy = Enemy()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                racket.dx = -7
            elif event.key == pygame.K_RIGHT:
                racket.dx = 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                racket.dx = 0

    screen.fill(BLUE)
    ball.update()
    enemy.update(ball)
    racket.update(ball)

    ball.draw(screen)
    enemy.draw(screen)
    racket.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
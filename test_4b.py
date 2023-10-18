import pygame, random, time

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
        self.dx = 6
        self.dy = 6
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

    def draw(self,screen):
        pygame.draw.rect(screen,WHITE,self.rect)

    def reset(self,x,y):
        self.rect.x = x
        self.rect.y = y
        if y < int(SCREEN_HEIGHT/2):
            self.dy = 6
        else:
            self.dy = -6
        self.dx = random.randint(-6,6)


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
            if self.dx > 0:
                ball.dx += 2
            elif self.dx < 0:
                ball.dx += -2
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
        if self.rect.centerx < ball.rect.centerx:
            diff_x = ball.rect.centerx - self.rect.centerx
            if diff_x > 6:
                self.rect.x += 6
            elif diff_x <= 6:
                self.rect.centerx = ball.rect.centerx
        elif self.rect.centerx > ball.rect.centerx:
            diff_x = self.rect.centerx - ball.rect.centerx
            if diff_x > 6:
                self.rect.x += -6
            elif diff_x <= 6:
                self.rect.centerx = ball.rect.centerx

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

    if ball.rect.y < 0:
        time.sleep(2)
        ball.reset(enemy.rect.centerx, enemy.rect.centery)
    elif ball.rect.y > SCREEN_HEIGHT:
        time.sleep(2)
        ball.reset(racket.rect.centerx,racket.rect.centery)

    ball.draw(screen)
    enemy.draw(screen)
    racket.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
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
        self.dx = 3
        self.dy = 3
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

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

ball = Ball()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLUE)
    ball.update()
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
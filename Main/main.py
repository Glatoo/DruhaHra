import pygame

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255,0,0)
PLAY = True
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Janko a Marienka')
clock = pygame.time.Clock()


def car(x, y):
    pygame.draw.rect(window, RED, (x, y, x + 50, y + 50), 2)


while PLAY:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False

    window.fill(WHITE)
    car(200, 200)
    pygame.display.update()
    clock.tick(60)





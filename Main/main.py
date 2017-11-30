import pygame

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
PLAY = True
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Janko a Marienka')
clock = pygame.time.Clock()


while PLAY:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False

    window.fill(WHITE)
    pygame.display.update()



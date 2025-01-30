import GameData
import pygame

pygame.init()


def loadingAnimation(screen):
    CLOCK = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

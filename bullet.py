import pygame
import UsageFunction

pygame.init()


class BULLET:
    def __init__(self, x, y, imagePath):
        self.x = x
        self.y = y
        self.imagePath = imagePath
        self.mask = pygame.mask.from_surface(self.imagePath)

    def loadBulletImage(self, screen):
        screen.blit(self.imagePath, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not (height >= self.y >= 0)

    def collision(self, obj):
        return UsageFunction.is_collision(self, obj)

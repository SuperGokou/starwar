import pygame
import GameData
import bullet
import enemy

pygame.init()


class Plane(object):

    def __init__(self, x, y, health=200):
        self.x = x
        self.y = y
        self.planeImage = None
        self.bulletImage = None
        self.bullets = []
        self.lasers = []
        self.laserImage = None
        self.count = 0
        self.health = health
        self.COOLDONW = 30

    def loadPlaneImage(self, screen):
        screen.blit(self.planeImage, (self.x, self.y))
        for blet in self.bullets:
            blet.loadBulletImage(screen)
        for laser in self.lasers:
            laser.loadBulletImage(screen)

    def cooldown(self):
        if self.count >= self.COOLDONW:
            self.count = 0
        elif self.count > 0:
            self.count += 1

    def shoot(self):
        if self.count == 0:
            width = self.planeImage.get_width()
            height = self.planeImage.get_height()
            blet = bullet.BULLET(self.x - 8 + width / 2, self.y - height / 2, self.bulletImage)
            laser = bullet.BULLET(self.x - 8 + width / 2, self.y - height / 2, self.bulletImage)
            self.bullets.append(laser)
            self.bullets.append(blet)
            self.count = 1

    def BULLET_MOVING(self, vel, objs):
        self.cooldown()
        for blet in self.bullets:
            blet.move(vel)
            if blet.off_screen(GameData.ScreenHeight):
                self.bullets.remove(blet)
            if blet.collision(objs):
                self.bullets.remove(blet)
                if isinstance(self, enemy.Enemy):
                    objs.health -= 30
                if isinstance(self, enemy.Enemy_BOSS):
                    objs.health -= 30 * GameData.level

    def width_plane(self):
        return self.planeImage.get_width()

    def height_plane(self):
        return self.planeImage.get_height()

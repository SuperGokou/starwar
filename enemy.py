import math
import random
import GameData
import bullet
import plane
import pygame

pygame.init()

RED_PLANE = pygame.image.load('images/enemiesplane/en1.png')
BLUE_PLANE = pygame.image.load('images/enemiesplane/en2.png')
YELLOW_PLANE = pygame.image.load('images/enemiesplane/en3.png')
RED_BULLET = pygame.image.load('images/enemiesplane/enb1.png')
BLUE_BULLET = pygame.image.load('images/enemiesplane/enb2.png')
YELLOW_BULLET = pygame.image.load('images/enemiesplane/enb3.png')
BOSS1 = pygame.image.load('images/boss/b1.png')
BOSS2 = pygame.image.load('images/boss/b2.png')
BOSS3 = pygame.image.load('images/boss/b3.png')
BOSS4 = pygame.image.load('images/boss/b4.png')
BOSS5 = pygame.image.load('images/boss/b5.png')
BOSS6 = pygame.image.load('images/boss/b6.png')
CIRCLEBULLET = pygame.image.load('images/boss/bb10.png')
RECTANBULLET = pygame.image.load('images/boss/bb11.png')

ROCKET1 = pygame.image.load('images/rocket/rk1.png')
ROCKET2 = pygame.image.load('images/rocket/rk2.png')
ROCKET3 = pygame.image.load('images/rocket/rk3.png')


class Enemy(plane.Plane):
    PLANE_MAP = {
        "RED": (RED_PLANE, RED_BULLET),
        "BLUE": (BLUE_PLANE, BLUE_BULLET),
        "YELLOW": (YELLOW_PLANE, YELLOW_BULLET)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.planeImage, self.bulletImage = self.PLANE_MAP[color]
        self.mask = pygame.mask.from_surface(self.planeImage)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.count == 0:
            width = self.planeImage.get_width()
            height = self.planeImage.get_height()
            blet1 = bullet.BULLET(self.x + -8 + width, self.y + height, self.bulletImage)
            blet2 = bullet.BULLET(self.x + -8, self.y + height, self.bulletImage)
            self.bullets.append(blet1)
            self.bullets.append(blet2)
            self.count = 1


class Enemy_BOSS(plane.Plane):
    up = True
    right = True
    vely = 2
    velx = 2
    PLANE_MAP = {
        "LEVEL1": (BOSS1, CIRCLEBULLET, RECTANBULLET),
        "LEVEL2": (BOSS2, CIRCLEBULLET, RECTANBULLET),
        "LEVEL3": (BOSS3, CIRCLEBULLET, RECTANBULLET),
        "LEVEL4": (BOSS4, CIRCLEBULLET, RECTANBULLET),
        "LEVEL5": (BOSS5, CIRCLEBULLET, RECTANBULLET),
        "LEVEL6": (BOSS6, CIRCLEBULLET, RECTANBULLET)
    }

    def __init__(self, x, y, color, health=3000):
        super().__init__(x, y, health)
        self.planeImage, self.bulletImage, self.laserImage = self.PLANE_MAP[color]
        self.mask = pygame.mask.from_surface(self.planeImage)
        self.max_health = health

    def move(self):
        if self.y < 200:
            self.vely = abs(self.vely)
            self.up = True
        if self.x < 100:
            self.velx = abs(self.velx)
            self.right = True
        if self.y > GameData.ScreenHeight - 500 and self.up:
            self.vely = -1 * self.vely
            self.up = False
        if self.x > GameData.ScreenWidth - 200 and self.right:
            self.velx = -1 * self.velx
            self.right = False
        self.y += self.vely
        self.x += self.velx

    def shoot(self):
        if self.count == 0:
            width = self.planeImage.get_width()
            height = self.planeImage.get_height()
            blet3 = bullet.BULLET(self.x + -8 + width, self.y + height, self.bulletImage)
            blet4 = bullet.BULLET(self.x + -8, self.y + height, self.bulletImage)
            self.bullets.append(blet3)
            self.bullets.append(blet4)
            self.count = 1

    def loadHealthBar(self, screen):
        super().loadPlaneImage(screen)
        self.healthbar_label(screen)

    def healthbar_label(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 10, self.planeImage.get_width(), 5))
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.x, self.y - 10, self.planeImage.get_width() * (self.health / self.max_health), 5))


class ROCKET(plane.Plane):
    PLANE_MAP = {
        "RED": (ROCKET1),
        "BLUE": (ROCKET2),
        "YELLOW": (ROCKET3)
    }

    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.planeImage = self.PLANE_MAP[color]
        self.mask = pygame.mask.from_surface(self.planeImage)
        self.angel = 0

    def move(self, vel, obj):
        if self.x < obj.x:
            self.x += vel
            self.angel = 30
        if self.x > obj.x:
            self.x -= vel
            self.angel = -30
        if self.x == obj.x:
            self.angel = 0
        # b = (self.y + obj.y)/math.pow((self.x - obj.x), 2)
        b = 1.5
        Vx = abs(self.x - vel)
        self.y += round(b * math.pow((Vx - self.x), 2))

    def loadRotation(self, screen):
        newimage = pygame.transform.rotate(self.planeImage, self.angel)
        screen.blit(newimage, (self.x, self.y))



import GameData
import enemy
import gaming
import plane
import pygame

pygame.init()

FIRE_BULLET = pygame.image.load('images/userairplane/shoot1.png')


class userPlayer(plane.Plane):
    def __init__(self, x, y, health=200):
        super().__init__(x, y, health)
        self.planeImage = GameData.PLANE
        self.bulletImage = FIRE_BULLET
        self.mask = pygame.mask.from_surface(self.planeImage)
        self.max_health = health

    def healthbar_label(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x, self.y + self.planeImage.get_height() + 10, self.planeImage.get_width(), 8))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y + self.planeImage.get_height() + 10,
                                               self.planeImage.get_width() * (self.health / self.max_health), 8))

    def loadHealthBar(self, screen):
        super().loadPlaneImage(screen)
        self.healthbar_label(screen)

    def BULLET_MOVING(self, vel, objs):
        self.cooldown()
        for blet in self.bullets:
            blet.move(vel)
            if blet.off_screen(GameData.ScreenHeight):
                self.bullets.remove(blet)
            else:
                for obj in objs:
                    if blet.collision(obj):
                        obj.health -= 30
                        if obj.health <= 0:
                            pygame.mixer.Sound.play(GameData.COLLISION_COUND)
                            objs.remove(obj)
                            if isinstance(obj, enemy.Enemy_BOSS):
                                GameData.score += GameData.BOSS_ENEMY_SCORE
                                GameData.level += 1
                            elif isinstance(obj, enemy.Enemy):
                                GameData.score += GameData.ENEMY_SCORE
                            elif isinstance(obj, enemy.ROCKET):
                                GameData.score += GameData.ENEMY_SCORE * 2

                        if blet in self.bullets:
                            self.bullets.remove(blet)
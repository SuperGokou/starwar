import random
import pygame
import UsageFunction
import enemy
import gameover
import menu
import player
import GameData
import wingame
import time

pygame.init()


def StartGame():
    run = True
    ENEMIES = []
    MAX_ENERMIES = 3
    ENERIES_MOVE_VEL = 2
    ENERIES_BULLET_VEL = 3
    ROCKET_VEL = 1
    PLAYER_BULLET_VEL = 6
    PLAYER_MOVE_VEL = 5
    BOSSES = []
    LEVELS = ['LEVEL1', 'LEVEL2', 'LEVEL3', 'LEVEL4', 'LEVEL5', 'LEVEL6']
    GameData.life = 5
    ROCKETS = []
    user_play = player.userPlayer(GameData.ScreenWidth / 2, GameData.ScreenHeight - 120)
    WARNING_BAR = GameData.menu_game_font.render(f"BOSS COMING", True, (225, 0, 0)).convert_alpha()

    def redraw_window(LEVEL):
        level_bar = GameData.gaming_text_ront.render(f"Level: {LEVEL}", True, (255, 255, 255))
        life_bar = GameData.gaming_text_ront.render(f"Live: {GameData.life}", True, (255, 255, 255))
        score_bar = GameData.gaming_text_ront.render(f"Score: {GameData.score}", True, (255, 255, 255))

        GameData.window.blit(GameData.GAMING_BACKGROUND, (0, 0))
        GameData.window.blit(life_bar, (GameData.ScreenWidth - life_bar.get_width() - 10, 10))
        GameData.window.blit(level_bar, (GameData.ScreenWidth - level_bar.get_width() - 10,
                                         10 + life_bar.get_height()))
        GameData.window.blit(score_bar, (GameData.ScreenWidth - score_bar.get_width() - 10,
                                         2 * (5 + life_bar.get_height())))

        for ENERMY in ENEMIES:
            ENERMY.loadPlaneImage(GameData.window)

        for ROCKET in ROCKETS:
            ROCKET.loadRotation(GameData.window)

        for BOSS in BOSSES:
            BOSS.loadHealthBar(GameData.window)
            if BOSS.y > -200:
                GameData.window.blit(WARNING_BAR, ((GameData.ScreenWidth - WARNING_BAR.get_width() - 50) / 2, 350))

        if GameData.MENU_BUTTON.loadButtonImage(GameData.window):
            GameData.window.blit(GameData.ENTRY_BACKGROUND, (0, 0))
            menu.loadingMenu()

        user_play.loadHealthBar(GameData.window)
        pygame.display.update()

    while run:
        GameData.clock.tick(GameData.FPS)

        difficult = 1 + round(GameData.level/3)*10

        if GameData.life <= 0:
            GameData.HISTORY_SCORE.append(GameData.score)
            GameData.score = 0
            gameover.loadingGameover()
            run = False

        if GameData.level > 6:
            GameData.HISTORY_SCORE.append(GameData.score)
            GameData.score = 0
            GameData.level = 1
            wingame.loadingGameover()
            run = False

        if user_play.health <= 0:
            GameData.life -= 1
            user_play.health += 200

        redraw_window(GameData.level)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
        # clear regular enemies
        if len(BOSSES) == 0:
            X_POSITION = random.randrange(10, GameData.ScreenWidth - 260)
            Y_POSITION = -3000
            BOSS = enemy.Enemy_BOSS(X_POSITION, Y_POSITION, LEVELS[GameData.level - 1])
            BOSSES.append(BOSS)

        if BOSS.y < -400:
            if len(ENEMIES) == 0:
                MAX_ENERMIES += GameData.level
                for i in range(MAX_ENERMIES):
                    X_POSITION = random.randrange(10, GameData.ScreenWidth - 210)
                    Y_POSITION = random.randrange(-1500, -100)
                    ENERMY = enemy.Enemy(X_POSITION, Y_POSITION, random.choice(['RED', 'BLUE', 'YELLOW']))
                    ENEMIES.append(ENERMY)

        if len(ROCKETS) == 0:
            X_POSITION = random.randrange(10, GameData.ScreenWidth - 210)
            Y_POSITION = -300 + 100 * difficult
            ROCKET = enemy.ROCKET(X_POSITION, Y_POSITION, random.choice(['RED', 'BLUE', 'YELLOW']))
            ROCKETS.append(ROCKET)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and user_play.x - PLAYER_MOVE_VEL > 0:
            user_play.x -= PLAYER_MOVE_VEL
        if keys[pygame.K_RIGHT] and user_play.x + PLAYER_MOVE_VEL + user_play.width_plane() < GameData.ScreenWidth:
            user_play.x += PLAYER_MOVE_VEL
        if keys[pygame.K_UP] and user_play.y - PLAYER_MOVE_VEL > 0:
            user_play.y -= PLAYER_MOVE_VEL
        if keys[
            pygame.K_DOWN] and user_play.y + PLAYER_MOVE_VEL + user_play.height_plane() + 20 < GameData.ScreenHeight:
            user_play.y += PLAYER_MOVE_VEL
        if keys[pygame.K_SPACE]:
            pygame.mixer.Sound.play(GameData.PLAYER_BULLET_SOUND)
            user_play.shoot()

        BOSS.move()
        BOSS.BULLET_MOVING(ENERIES_BULLET_VEL, user_play)

        ROCKET.move(ROCKET_VEL, user_play)

        for ENERMY in ENEMIES:
            ENERMY.move(ENERIES_MOVE_VEL)
            ENERMY.BULLET_MOVING(ENERIES_BULLET_VEL, user_play)

            if random.randrange(0, round(100/difficult)) == 1:
                pygame.mixer.Sound.play(GameData.ENEMY_BULLET_COUND)
                ENERMY.shoot()
                BOSS.shoot()
            if UsageFunction.is_collision(ENERMY, user_play):
                user_play.health -= 20
                pygame.mixer.Sound.play(GameData.COLLISION_COUND)
                ENEMIES.remove(ENERMY)
                GameData.score += GameData.ENEMY_SCORE
            if ENERMY.y - ENERMY.height_plane() > GameData.ScreenHeight:
                ENEMIES.remove(ENERMY)

        if ROCKET.y - ROCKET.height_plane() > GameData.ScreenHeight:
            ROCKETS.remove(ROCKET)

        if UsageFunction.is_collision(BOSS, user_play):
            user_play.health = 0
            pygame.mixer.Sound.play(GameData.COLLISION_COUND)
            user_play.x = GameData.ScreenWidth / 2
            user_play.y = GameData.ScreenHeight - 120

        if UsageFunction.is_collision(ROCKET, user_play):
            user_play.health -= 50
            pygame.mixer.Sound.play(GameData.COLLISION_COUND)
            ROCKETS.remove(ROCKET)

        user_play.BULLET_MOVING(-1 * PLAYER_BULLET_VEL, ENEMIES)
        user_play.BULLET_MOVING(-1 * PLAYER_BULLET_VEL, BOSSES)
        user_play.BULLET_MOVING(-1 * PLAYER_BULLET_VEL, ROCKETS)


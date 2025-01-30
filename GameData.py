import pygame
import menubutton
import selectplane

pygame.init()

# Basic UI data setting
LOADINGBARWORK = 10000000
Icon = pygame.image.load("images/icons/GameIcon.jpg")
ScreenWidth, ScreenHeight = 720, 800
window = pygame.display.set_mode((ScreenWidth, ScreenHeight))

#video in game



# background images
ENTRY_BACKGROUND = pygame.image.load('images/background/entrybg.png')
GAMING_BACKGROUND = pygame.image.load('images/background/background.jpg')
LEVEL_BACKGROUND = pygame.image.load('images/background/bglevel.png')
SELECT_BACKGROUND = pygame.image.load('images/background/chooseplane.png')


# garment
menu_game_font = pygame.font.Font('font/Gamix.ttf', 35)
gaming_text_ront = pygame.font.SysFont('Arial Black', 25)
level_text_ront = pygame.font.Font('font/Gamix.ttf', 40)
historyscore_text_ront = pygame.font.Font('font/DeathStar.otf', 35)


# plane Images and bullet
PLANE = pygame.image.load('images/userairplane/plane0.png')
PLANE1 = pygame.image.load('images/userairplane/plane0.png')
PLANE2 = pygame.image.load('images/userairplane/plane1.png')
PLANE3 = pygame.image.load('images/userairplane/plane2.png')
PLANE4 = pygame.image.load('images/userairplane/plane3.png')
PLANE5 = pygame.image.load('images/userairplane/plane4.png')
PLANE6 = pygame.image.load('images/userairplane/plane5.png')


# Music
BG_MUSIC = pygame.mixer.Sound('sounds/bkmusic.mp3')
PLAYER_BULLET_SOUND = pygame.mixer.Sound('sounds/bullet.wav')
ENEMY_BULLET_COUND = pygame.mixer.Sound('sounds/bullet.wav')
COLLISION_COUND = pygame.mixer.Sound('sounds/collision.wav')


#menu button
MENU = gaming_text_ront.render(f"MENU", True, (225, 255, 255))
MENU_BUTTON = menubutton.BUTTON(10, 10, MENU)

#Gaming data
clock = pygame.time.Clock()
FPS = 60
life = 5
level = 1
score = 0

#History Score
HISTORY_SCORE = []

#enemy plane and bullet
ENEMY_SCORE = 50
BOSS_ENEMY_SCORE = 500

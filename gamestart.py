import pygame
import GameData
import menu
from moviepy.editor import *

pygame.init()

# set up the window size and title bar
Icon = pygame.image.load("images/icons/GameIcon.jpg")
pygame.display.set_icon(Icon)
pygame.display.set_caption("Star War Aircaft 2021.V1.0")
clock = pygame.time.Clock()



def main():
    TITLE_LABEL = GameData.menu_game_font.render("PRESS ANY TO START GAME ", True, (255, 255, 0))
    X_POSITION = round(GameData.ScreenWidth - TITLE_LABEL.get_width() - 8) / 2
    Y_POSITION = GameData.ScreenHeight * 2 / 3
    GameData.window.blit(GameData.ENTRY_BACKGROUND, (0, 0))
    GameData.window.blit(TITLE_LABEL, (X_POSITION, Y_POSITION))
    pygame.mixer.Sound.play(GameData.BG_MUSIC, -1)
    # clock.tick(120)
    run = True
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            # if event.type == pygame.VIDEORESIZE:
            #     old_window = GameData.window
            #     GameData.window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            #     GameData.window.blit(old_window, (0, 0))
            #     del old_window
            if event.type == pygame.KEYDOWN:
                GameData.window.blit(GameData.ENTRY_BACKGROUND, (0, 0))
                menu.loadingMenu()
                break
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()

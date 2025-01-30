import GameData
import menubutton
import pygame
import selectlevel
import selectplane
import historyscore

pygame.init()


def loadingMenu():
    # loading all images and font
    ENTRY_MENU = GameData.menu_game_font.render(f"NEW GAME", True, (225, 0, 0)).convert_alpha()
    LEVEL_MENU = GameData.menu_game_font.render(f"LEVEL ENTRY", True, (225, 0, 0)).convert_alpha()
    SCORE_MENU = GameData.menu_game_font.render(f"HISTORY SCORE", True, (225, 0, 0)).convert_alpha()

    X_POSITION = round(GameData.ScreenWidth - ENTRY_MENU.get_width() - 10) / 2
    Y_POSITION = GameData.ScreenHeight * 2 / 3
    ENTRY_MENU_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, ENTRY_MENU)

    X_POSITION = round(GameData.ScreenWidth - LEVEL_MENU.get_width() - 10) / 2
    Y_POSITION = Y_POSITION + ENTRY_MENU.get_height() + 40
    LEVEL_MENU_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, LEVEL_MENU)

    X_POSITION = round(GameData.ScreenWidth - SCORE_MENU.get_width() - 10) / 2
    Y_POSITION = Y_POSITION + LEVEL_MENU.get_height() + 40
    SCORE_MENU_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, SCORE_MENU)

    run = True
    while run:
        GameData.clock.tick(GameData.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        if ENTRY_MENU_BUTTON.loadButtonImage(GameData.window):
            GameData.level = 1
            selectplane.loadingPlane()
            break

        if LEVEL_MENU_BUTTON.loadButtonImage(GameData.window):
            selectlevel.loadingLevel()
            break

        if SCORE_MENU_BUTTON.loadButtonImage(GameData.window):
            historyscore.loadingScore()
            break

        pygame.display.update()


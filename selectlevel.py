import GameData
import menubutton
import pygame
import menu
import selectplane

pygame.init()


def loadingLevel():
    # loading all images and font
    L1 = GameData.level_text_ront.render(f"LEVEL      I", True, (225, 255, 255)).convert_alpha()
    L2 = GameData.level_text_ront.render(f"LEVEL      II", True, (225, 255, 255)).convert_alpha()
    L3 = GameData.level_text_ront.render(f"LEVEL      III", True, (225, 255, 255)).convert_alpha()
    L4 = GameData.level_text_ront.render(f"LEVEL      IIII", True, (225, 255, 255)).convert_alpha()
    L5 = GameData.level_text_ront.render(f"LEVEL      V", True, (225, 255, 255)).convert_alpha()
    L6 = GameData.level_text_ront.render(f"LEVEL      VI", True, (225, 255, 255)).convert_alpha()

    X_POSITION = round(GameData.ScreenWidth - L1.get_width() - 10) / 3
    Y_POSITION = 100
    L1_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, L1)

    Y_POSITION = Y_POSITION + L2.get_height() + 30
    L2_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, L2)

    Y_POSITION = Y_POSITION + L3.get_height() + 30
    L3_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, L3)

    Y_POSITION = Y_POSITION + L3.get_height() + 30
    L4_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, L4)

    Y_POSITION = Y_POSITION + L4.get_height() + 30
    L5_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, L5)

    Y_POSITION = Y_POSITION + L5.get_height() + 30
    L6_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, L6)

    run = True
    while run:
        GameData.clock.tick(GameData.FPS)
        GameData.window.blit(GameData.LEVEL_BACKGROUND, (0, 0))

        if GameData.MENU_BUTTON.loadButtonImage(GameData.window):
            GameData.window.blit(GameData.ENTRY_BACKGROUND, (0, 0))
            menu.loadingMenu()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        if L1_BUTTON.loadButtonImage(GameData.window):
            GameData.level = 1
            selectplane.loadingPlane()
            break

        if L2_BUTTON.loadButtonImage(GameData.window):
            GameData.level = 2
            selectplane.loadingPlane()
            break

        if L3_BUTTON.loadButtonImage(GameData.window):
            GameData.level = 3
            selectplane.loadingPlane()
            break

        if L4_BUTTON.loadButtonImage(GameData.window):
            GameData.level = 4
            selectplane.loadingPlane()
            break

        if L5_BUTTON.loadButtonImage(GameData.window):
            GameData.level = 5
            selectplane.loadingPlane()
            break

        if L6_BUTTON.loadButtonImage(GameData.window):
            GameData.level = 6
            selectplane.loadingPlane()
            break

        pygame.display.update()

import pygame
import GameData
import menu

pygame.init()


def loadingGameover():
    GameData.window.blit(GameData.GAMING_BACKGROUND, (0, 0))

    YOU_WIN = GameData.menu_game_font.render(f"CONGRATS YOU WIN THE GAME", True, (225, 255, 0)).convert_alpha()
    CLICK_MENU = GameData.menu_game_font.render(f"PLEASE CLICK MENU", True, (225, 255, 0)).convert_alpha()

    GameData.window.blit(YOU_WIN, ((GameData.ScreenWidth - YOU_WIN.get_width() - 50) / 2, 550))
    GameData.window.blit(CLICK_MENU, ((GameData.ScreenWidth - CLICK_MENU.get_width() - 50) / 2, 650))

    run = True
    while run:
        GameData.clock.tick(GameData.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        if GameData.MENU_BUTTON.loadButtonImage(GameData.window):
            GameData.window.blit(GameData.ENTRY_BACKGROUND, (0, 0))
            menu.loadingMenu()

        pygame.display.update()
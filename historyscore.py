import GameData
import pygame
import menubutton
import menu
import gaming


def loadingScore():
    Y = 100
    GameData.window.blit(GameData.LEVEL_BACKGROUND, (0, 0))
    Title = GameData.level_text_ront.render(f"History Score", True, (225, 255, 255)).convert_alpha()
    GameData.window.blit(Title, ((GameData.ScreenWidth - Title.get_width() - 50)/2, 20))

    i = 1
    for score in GameData.HISTORY_SCORE[:10]:
        S = GameData.historyscore_text_ront.render(f"# {i}     Score:      {score}", True, (225, 255, 255)).convert_alpha()
        Y += S.get_height() + 30
        i += 1
        GameData.window.blit(S, (GameData.ScreenWidth - 750, 10 + Y))

    run = True
    while run:
        GameData.clock.tick(GameData.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

            if GameData.MENU_BUTTON.loadButtonImage(GameData.window):
                GameData.window.blit(GameData.ENTRY_BACKGROUND, (0, 0))
                menu.loadingMenu()
                break

        pygame.display.update()
import GameData
import pygame
import menubutton
import menu
import gaming
import tkinter.messagebox

pygame.init()


def loadingPlane():
    Start = GameData.level_text_ront.render(f"Start", True, (225, 255, 255)).convert_alpha()
    X_POSITION = GameData.ScreenWidth - Start.get_width() - 100
    Y_POSITION = GameData.ScreenHeight - 150
    Start_BUTTON = menubutton.BUTTON(X_POSITION, Y_POSITION, Start)

    # poison of each plane

    X_POSITION = 102
    Y_POSITION = 225
    ImagePlane1 = menubutton.IMAGE_BUTTON(X_POSITION, Y_POSITION, GameData.PLANE1)
    X_POSITION = 331
    ImagePlane2 = menubutton.IMAGE_BUTTON(X_POSITION, Y_POSITION, GameData.PLANE2)
    X_POSITION = 560
    ImagePlane3 = menubutton.IMAGE_BUTTON(X_POSITION, Y_POSITION, GameData.PLANE3)
    X_POSITION = 102
    Y_POSITION = 371
    ImagePlane4 = menubutton.IMAGE_BUTTON(X_POSITION, Y_POSITION, GameData.PLANE4)
    X_POSITION = 331
    ImagePlane5 = menubutton.IMAGE_BUTTON(X_POSITION, Y_POSITION, GameData.PLANE5)
    X_POSITION = 560
    ImagePlane6 = menubutton.IMAGE_BUTTON(X_POSITION, Y_POSITION, GameData.PLANE6)

    # poison of each plane

    run = True
    click = click1 = click2 = click3 = click4 = click5 = click6 = 0
    while run:
        GameData.clock.tick(GameData.FPS)
        GameData.window.blit(GameData.SELECT_BACKGROUND, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        if ImagePlane1.loadButtonImage(GameData.window):
            click1 += 1
            if click1 % 2 == 0:
                click1 = 0
            else:
                GameData.PLANE = pygame.image.load('images/userairplane/plane0.png')
                click1 = 1

        if ImagePlane2.loadButtonImage(GameData.window):
            click2 += 1
            if click2 % 2 == 0:
                click2 = 0
            else:
                GameData.PLANE = pygame.image.load('images/userairplane/plane1.png')
                click2 = 1

        if ImagePlane3.loadButtonImage(GameData.window):
            click3 += 1
            if click3 % 2 == 0:
                click3 = 0
            else:
                GameData.PLANE = pygame.image.load('images/userairplane/plane2.png')
                click3 = 1

        if ImagePlane4.loadButtonImage(GameData.window):
            click4 += 1
            if click4 % 2 == 0:
                click4 = 0
            else:
                GameData.PLANE = pygame.image.load('images/userairplane/plane3.png')
                click4 = 1

        if ImagePlane5.loadButtonImage(GameData.window):
            click5 += 1
            if click5 % 2 == 0:
                click5 = 0
            else:
                GameData.PLANE = pygame.image.load('images/userairplane/plane4.png')
                click5 = 1

        if ImagePlane6.loadButtonImage(GameData.window):
            click6 += 1
            if click6 % 2 == 0:
                click6 = 0
            else:
                GameData.PLANE = pygame.image.load('images/userairplane/plane5.png')
                click6 = 1

        if Start_BUTTON.loadButtonImage(GameData.window):
            # check click time
            click = click1 + click2 + click3 + click4 + click5 + click6
            if click > 1:
                root = tkinter.Tk()
                root.withdraw()
                tkinter.messagebox.showwarning("WARNING", "Only One Plane Can Be Select!")
                click = click1 = click2 = click3 = click4 = click5 = click6 = 0
            else:
                gaming.StartGame()
                break

        if GameData.MENU_BUTTON.loadButtonImage(GameData.window):
            GameData.window.blit(GameData.ENTRY_BACKGROUND, (0, 0))
            menu.loadingMenu()
            break

        pygame.display.update()

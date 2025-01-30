import pygame

pygame.init()


class BUTTON(object):
    def __init__(self, x, y, text):
        self.text = text
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)
        self.click = False
        self.top_color = '#2c2c2c'

    def loadButtonImage(self, screen):
        action = False
        # get the position of the click area
        POSITION = pygame.mouse.get_pos()

        if self.rect.collidepoint(POSITION):
            self.top_color = '#DCF0EF'
            if pygame.mouse.get_pressed()[0] and not self.click:
                self.click = True
                action = True
        else:
            self.top_color = '#2c2c2c'

        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False

        pygame.draw.rect(screen, self.top_color, self.rect)
        screen.blit(self.text, (self.rect.x, self.rect.y))
        return action


class IMAGE_BUTTON(object):

    def __init__(self, x, y, text):
        self.text = text
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)
        self.click = False
        self.top_color = '#2c2c2c'
        self.count = 0

    def loadButtonImage(self, screen):
        action = False
        # get the position of the click area
        POSITION = pygame.mouse.get_pos()

        if self.rect.collidepoint(POSITION):
            if pygame.mouse.get_pressed()[0] and not self.click:
                self.count += 1
                if self.count % 2 == 0:
                    self.top_color = '#2c2c2c'
                else:
                    self.top_color = '#DCF0EF'
                self.click = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False

        pygame.draw.rect(screen, self.top_color, self.rect)
        screen.blit(self.text, (self.rect.x, self.rect.y))
        return action

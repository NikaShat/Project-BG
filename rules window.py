import pygame


class Rules_Window():
    def __init__(self):
        pygame.init()
        self.size = 600, 600
        self.screen = pygame.display.set_mode(self.size)

    def draw(self):
        pass


pygame.quit()

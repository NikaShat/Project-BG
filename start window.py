import pygame

WIDTH = 600
HEIGHT = 600


class Start_Window():
    def __init__(self):
        pygame.init()
        self.size = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode(self.size)

    def draw(self):
        pass


window = Start_Window()

pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

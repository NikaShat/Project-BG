import pygame


class Levels_Window:
    def __init__(self):
        pygame.init()

    def draw(self):
        image = self.load_image('levels window.jpg')
        screen.blit(image, (0, 0))


pygame.quit()
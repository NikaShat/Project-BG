import pygame
import os


class Rules_Window():
    def __init__(self):
        pygame.init()

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname).convert()
        return image

    def draw(self):
        image = self.load_image('rules window.jpg')
        screen.blit(image, (0, 0))


pygame.quit()

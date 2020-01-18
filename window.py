import pygame
import load_image


class Window:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen

    def draw(self, image_name):
        image = load_image.loadimage(image_name)
        self.screen.blit(image, (0, 0))

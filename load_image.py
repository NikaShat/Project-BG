import pygame
import os


# загрузка картинки
def loadimage(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image

import pygame


class Player_Window:
    def __init__(self):
        pygame.init()

    def draw(self):
        image = self.load_image('player window.jpg')
        screen.blit(image, (0, 0))


pygame.quit()

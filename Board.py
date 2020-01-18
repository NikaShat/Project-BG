import pygame


class Board:
    def __init__(self):
        self.width = 12
        self.height = 12
        self.board = [[0] * 12 for _ in range(12)]
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 50

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                                 x * self.cell_size + self.left, y * self.cell_size + self.top,
                                 self.cell_size, self.cell_size), 1)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)

    def get_cell(self, mouse_pos):
        coord_x = (mouse_pos[0] - self.left) // self.cell_size
        coord_y = (mouse_pos[1] - self.left) // self.cell_size
        coord = coord_x, coord_y
        return coord

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

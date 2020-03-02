import pygame
import load_image
import classes
import enemies

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level, player_group, tiles_group, all_sprites, level_num,
                   classess, collide, not_collide,
                   health_group, money_group, exit_group, enemy_group, cur):
    if level_num == 1:
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == 'x':
                    Tile('cantgo', x, y, 1, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == '-':
                    Tile('earth', x, y, 1, tiles_group, all_sprites, collide)
                elif level[y][x] == '*':
                    Tile('earth', x, y, 1, tiles_group, all_sprites, collide)
                    HealthMoneyExit(x, y, health_group, all_sprites,
                                    1, 'heart')
                elif level[y][x] == 'r':
                    Tile('river', x, y, 1, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == 'b':
                    Tile('bridge', x, y, 1, tiles_group, all_sprites, collide)
                elif level[y][x] == '^':
                    Tile('forest', x, y, 1, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == '$':
                    Tile('earth', x, y, 1, tiles_group, all_sprites, collide)
                    HealthMoneyExit(x, y, money_group, all_sprites, 1, 'money')
                elif level[y][x] == '+':
                    Tile('mountain', x, y, 1, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == '!':
                    Tile('exit', x, y, 1, tiles_group, all_sprites, collide)
                    HealthMoneyExit(x, y, exit_group, all_sprites, 1, 'exit')
                elif level[y][x] == '@':
                    Tile('earth', x, y, 1, tiles_group, all_sprites, collide)
                    hero = classes.Hero(player_group, all_sprites, classess,
                                        x, y, cur, True)
                elif level[y][x] == '#':
                    Tile('earth', x, y, 1, tiles_group, all_sprites, collide)
                    enemy = enemies.Enemy(enemy_group, all_sprites, 'animal',
                                          x, y, cur, True)
    elif level_num == 2:
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == 'x':
                    Tile('cantgo', x, y, 2, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == '-':
                    Tile('sand', x, y, 2, tiles_group, all_sprites, collide)
                elif level[y][x] == '*':
                    Tile('sand', x, y, 2, tiles_group, all_sprites, collide)
                    HealthMoneyExit(x, y, health_group, all_sprites,
                                    2, 'heart')
                elif level[y][x] == '^':
                    Tile('ruins', x, y, 2, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == 'b':
                    Tile('bridge', x, y, 2, tiles_group, all_sprites, collide)
                elif level[y][x] == '=':
                    Tile('cliff', x, y, 2, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == '$':
                    Tile('sand', x, y, 2, tiles_group, all_sprites, collide)
                    HealthMoneyExit(x, y, money_group, all_sprites, 2, 'money')
                elif level[y][x] == '+':
                    Tile('mountain', x, y, 2, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == '%':
                    Tile('plant', x, y, 2, tiles_group, all_sprites, collide)
                elif level[y][x] == '!':
                    Tile('exit', x, y, 2, tiles_group, all_sprites, collide)
                    HealthMoneyExit(x, y, exit_group, all_sprites, 2, 'exit')
                elif level[y][x] == '@':
                    Tile('sand', x, y, 2, tiles_group, all_sprites, collide)
                    hero = classes.Hero(player_group, all_sprites, classess,
                                        x, y, cur, True)
                elif level[y][x] == '#':
                    Tile('sand', x, y, 2, tiles_group, all_sprites, collide)
                    enemy = enemies.Enemy(enemy_group, all_sprites, 'worm',
                                          x, y, cur, True)
    else:
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == 'x':
                    Tile('cantgo', x, y, 3, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == '-':
                    Tile('swamp', x, y, 3, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == '*':
                    Tile('bridge', x, y, 3, tiles_group, all_sprites, collide)
                    HealthMoneyExit(x, y, health_group, all_sprites, 3,
                                    'heart')
                elif level[y][x] == '+':
                    Tile('wall', x, y, 3, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == 'b':
                    Tile('earth', x, y, 3, tiles_group, all_sprites, collide)
                elif level[y][x] == '^':
                    Tile('bridge', x, y, 3, tiles_group, all_sprites, collide)
                elif level[y][x] == '$':
                    Tile('bridge', x, y, 3, tiles_group, all_sprites, collide)
                    HealthMoneyExit(x, y, money_group, all_sprites, 3, 'money')
                elif level[y][x] == 'o':
                    Tile('crack', x, y, 3, tiles_group, all_sprites,
                         not_collide)
                elif level[y][x] == '!':
                    Tile('exit', x, y, 3, tiles_group, all_sprites, collide)
                    HealthMoneyExit(x, y, exit_group, all_sprites, 3, 'exit')
                elif level[y][x] == '@':
                    Tile('earth', x, y, 3, tiles_group, all_sprites, collide)
                    hero = classes.Hero(player_group, all_sprites, classess,
                                        x, y, cur, True)
                elif level[y][x] == '#':
                    Tile('bridge', x, y, 3, tiles_group, all_sprites, collide)
                    enemy = enemies.Enemy(enemy_group, all_sprites, 'skeleton',
                                          x, y, cur, True)
    return hero, x, y


tile_images_level1 = {'cantgo': load_image.loadimage('image_level1/cantgo1.png'),
                      'earth': load_image.loadimage('image_level1/earth1.png'),
                      'heart': load_image.loadimage('image_level1/heart1.png'),
                      'river': load_image.loadimage('image_level1/river.png'),
                      'bridge': load_image.loadimage('image_level1/bridge1.png'),
                      'money': load_image.loadimage('image_level1/money1.png'),
                      'forest': load_image.loadimage('image_level1/forest.png'),
                      'mountain': load_image.loadimage('image_level1/mountain1.png'),
                      'exit': load_image.loadimage('exit.png')}
tile_images_level2 = {'cantgo': load_image.loadimage('image_level2/cantgo2.png'),
                      'sand': load_image.loadimage('image_level2/sand.png'),
                      'heart': load_image.loadimage('image_level2/heart2.png'),
                      'ruins': load_image.loadimage('image_level2/ruins.png'),
                      'cliff': load_image.loadimage('image_level2/cliff.png'),
                      'money': load_image.loadimage('image_level2/money2.png'),
                      'bridge': load_image.loadimage('image_level1/bridge1.png'),
                      'mountain': load_image.loadimage('image_level2/mountain2.png'),
                      'plant': load_image.loadimage('image_level2/plant.png'),
                      'exit': load_image.loadimage('exit.png')}
tile_images_level3 = {'cantgo': load_image.loadimage('image_level3/cantgo3.png'),
                      'earth': load_image.loadimage('image_level3/earth3.png'),
                      'heart': load_image.loadimage('image_level3/heart3.png'),
                      'wall': load_image.loadimage('image_level3/wall.png'),
                      'bridge': load_image.loadimage('image_level3/bridge3.png'),
                      'money': load_image.loadimage('image_level3/money3.png'),
                      'crack': load_image.loadimage('image_level3/crack.png'),
                      'swamp': load_image.loadimage('image_level3/swamp.png'),
                      'exit': load_image.loadimage('exit.png')}

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, level_num,
                 tiles_group, all_sprites, group_collide):
        super().__init__(tiles_group, all_sprites, group_collide)
        if level_num == 1:
            self.image = tile_images_level1[tile_type]
        elif level_num == 2:
            self.image = tile_images_level2[tile_type]
        else:
            self.image = tile_images_level3[tile_type]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)


class HealthMoneyExit(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group, all_sprites, level_num, tile_type):
        super().__init__(group, all_sprites)
        if level_num == 1:
            self.image = tile_images_level1[tile_type]
        elif level_num == 2:
            self.image = tile_images_level2[tile_type]
        else:
            self.image = tile_images_level3[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x,
                                               tile_height * pos_y)

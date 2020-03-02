import pygame
import load_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_group, all_sprites, name, pos_x,
                 pos_y, cur, level_window):
        super().__init__(enemy_group, all_sprites)
        self.cur = cur  # подключение к БД
        self.quant_move = 0  # счетчик изменения картинки для анимации
        # статы персонажа
        self.health = (self.cur.execute(f"""SELECT health
                    FROM enemies
                    WHERE name = '{name}'""").fetchall())[0][0]
        self.max_health = self.health
        self.strength = (self.cur.execute(f"""SELECT strength
                    FROM enemies
                    WHERE name = '{name}'""").fetchall())[0][0]
        self.defence = (self.cur.execute(f"""SELECT defence
                    FROM enemies
                    WHERE name = '{name}'""").fetchall())[0][0]
        self.float_defence = (101 - self.defence) / 100
        self.speed = (self.cur.execute(f"""SELECT health
                    FROM enemies
                    WHERE name = '{name}'""").fetchall())[0][0]
        # имя врага
        self.name = name

        if level_window:
            if name == 'animal':
                self.image = load_image.loadimage("wolf/0.png")
                self.move_animation = [load_image.loadimage("wolf/1.png"),
                                       load_image.loadimage("wolf/2.png")]
            elif name == 'worm':
                self.image = load_image.loadimage("worm/0.png")
                self.move_animation = [load_image.loadimage("worm/1.png"),
                                       load_image.loadimage("worm/2.png")]
            elif name == 'skeleton':
                self.image = load_image.loadimage("skeleton/0.png")
                self.move_animation = [load_image.loadimage("skeleton/1.png"),
                                       load_image.loadimage("skeleton/2.png")]
            self.rect = self.image.get_rect().move(50 * pos_x, 50 * pos_y)
            print(self.rect)

    # наносимый урон
    def damage(self, damage):
        self.health -= int(damage * self.float_defence)
        if self.health <= 0:
            self.kill()

    def animation_move(self):
        self.quant_move = (self.quant_move + 1) % 2
        self.image = self.move_animation[self.quant_move]

import pygame, load_image, hero_presentation


class Hero(pygame.sprite.Sprite):
    def __init__(self, player_group, all_sprites, classes, pos_x, pos_y, cur, level_window):
        super().__init__(player_group, all_sprites)
        self.cur = cur  # подключение к БД
        self.quant_move = 0  # счетчик изменения картинки для анимации
        # статы персонажа
        self.health = (self.cur.execute(f"""SELECT health FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
        self.max_health = self.health
        self.strength = (self.cur.execute(f"""SELECT strength FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
        self.defence = (self.cur.execute(f"""SELECT defence FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
        self.float_defence = (101 - self.defence) / 100  # процент наносимого урона
        self.speed = (self.cur.execute(f"""SELECT speed FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
        self.intell = (self.cur.execute(f"""SELECT intelligence FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
        # тип класса, к которому относится персонаж
        self.classe = classes

        # подгрузка картинки и анимация
        if level_window:
            if classes == 'wizard':
                self.image = load_image.loadimage("wizard/0.png")
                self.move_animation = [load_image.loadimage("wizard/1.png"), load_image.loadimage("wizard/2.png")]
            elif classes == 'archer':
                self.image = load_image.loadimage("archer/0.png")
                self.move_animation = [load_image.loadimage("archer/1.png"), load_image.loadimage("archer/2.png")]
            elif classes == 'barbarian':
                self.image = load_image.loadimage("barbarian/0.png")
                self.move_animation = [load_image.loadimage("barbarian/1.png"), load_image.loadimage("barbarian/2.png")]
            elif classes == 'crusader':
                self.image = load_image.loadimage("crusader/0.png")
                self.move_animation = [load_image.loadimage("crusader/1.png"), load_image.loadimage("crusader/2.png")]
            elif classes == 'necromancer':
                self.image = load_image.loadimage("necromancer/0.png")
                self.move_animation = [load_image.loadimage("necromancer/1.png"), load_image.loadimage("necromancer/2.png")]
            self.rect = self.image.get_rect().move(50 * pos_x, 50 * pos_y)

    # наносимый урон
    def damage(self, damage):
        self.health -= int(damage * self.float_defence)

    # восстановление
    def healing(self):
        self.health = self.max_health

    # улучшение персонажа
    def upgrade(self, money, screen):
        money -= 100
        self.health += 1
        self.strength += 1
        self.defence += 1
        self.float_defence = (101 - self.defence) / 100
        self.speed += 1
        self.intell += 1
        self.cur.execute(f"""UPDATE classes
                        SET speed = {self.speed}
                        WHERE name = '{self.classe}'""").fetchall()
        self.cur.execute(f"""UPDATE classes 
                        SET intelligence = {self.intell}
                        WHERE name = '{self.classe}'""").fetchall()
        self.cur.execute(f"""UPDATE classes 
                        SET defence = {self.defence}
                        WHERE name = '{self.classe}'""").fetchall()
        self.cur.execute(f"""UPDATE classes 
                        SET strength = {self.strength}
                        WHERE name = '{self.classe}'""").fetchall()
        self.cur.execute(f"""UPDATE classes 
                        SET health = {self.health}
                        WHERE name = '{self.classe}'""").fetchall()
        self.cur.execute(f"""UPDATE player
                        SET money = {money}
                        WHERE key = 1""").fetchall()
        hero_presentation.presentation(self.classe, screen, self.cur)

    # пересечение с клетками (проходимые/непроходимые, клетки с монетами или жизнями)
    def update(self, tiles_group_not_collide, tiles_group_collide, health_group, money_group, exit_group):
        self.quant_move = (self.quant_move + 1) % 2
        self.image = self.move_animation[self.quant_move]
        flag_collide = bool
        flag_health = False
        flag_money = False
        flag_exit = False
        if pygame.sprite.spritecollideany(self, tiles_group_not_collide):
            flag_collide = False
        elif pygame.sprite.spritecollideany(self, tiles_group_collide):
            flag_collide = True
        if pygame.sprite.spritecollideany(self, health_group):
            sprite = pygame.sprite.spritecollideany(self, health_group)
            sprite.kill()
            flag_health = True
        if pygame.sprite.spritecollideany(self, money_group):
            sprite = pygame.sprite.spritecollideany(self, money_group)
            sprite.kill()
            flag_money = True
        if pygame.sprite.spritecollideany(self, exit_group):
            flag_exit = True
        return flag_collide, flag_health, flag_money, flag_exit

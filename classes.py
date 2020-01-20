import pygame, load_image, sqlite3

con = sqlite3.connect("data/database.db")
cur = con.cursor()


class Hero(pygame.sprite.Sprite):
    def __init__(self, player_group, all_sprites, classes, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.health = (cur.execute(f"""SELECT health FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
        self.strength = (cur.execute(f"""SELECT strength FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
        self.defence = (cur.execute(f"""SELECT defence FROM classes WHERE name = '{classes}'""").fetchall())[0][0]
        self.float_defence = (101 - self.defence) / 100
        self.speed = (cur.execute(f"""SELECT health FROM classes WHERE name = '{classes}'""").fetchall())[0][0]

        if classes == 'wizard':
            self.image = load_image.loadimage("wizard.png")
        elif classes == 'archer':
            self.image = load_image.loadimage("archer.png")
        elif classes == 'barbarian':
            self.image = load_image.loadimage("barbarian.png")
        elif classes == 'crusader':
            self.image = load_image.loadimage("crusader.png")
        elif classes == 'necromancer':
            self.image = load_image.loadimage("necromancer.png")

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect().move(50 * pos_x, 50 * pos_y)

    def damage(self, damage):
        self.health -= int(damage * self.float_defence)

    def healing(self, hp):
        if self.health + hp > 100:
            self.health = 100
        else:
            self.health += hp

    def upgrade(self):
        self.health += 1
        self.strength += 1
        self.defence += 1
        self.defence = (101 - self.defence) / 100
        self.speed += 1

    def update(self, tiles_group_not_collide, tiles_group_collide):
        if pygame.sprite.spritecollideany(self, tiles_group_not_collide):
            return False
        elif pygame.sprite.spritecollideany(self, tiles_group_collide):
            return True

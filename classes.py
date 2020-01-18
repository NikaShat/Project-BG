import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, group, health, strength, defence, speed, attack_range, image):
        super().__init__(group)
        self.health = health
        self.strength = strength
        self.defence = defence
        self.float_defence = (101 - defence) / 100
        self.speed = speed
        self.attack_range = attack_range
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def move_up(self):
        self.rect = self.rect.move(self.rect.x, self.rect.y - 50)

    def move_down(self):
        self.rect = self.rect.move(self.rect.x, self.rect.y + 50)

    def move_right(self):
        self.rect = self.rect.move(self.rect.x + 50, self.rect.y)

    def move_left(self):
        self.rect = self.rect.move(self.rect.x - 50, self.rect.y)

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


class Wizard(Hero):
    def __init__(self, group, health, strength, defence, speed, attack_range):
        self.image = load_image("wizard.png")
        super().__init__(group, health, strength, defence, speed, attack_range, self.image)


class Archer(Hero):
    def __init__(self, group, health, strength, defence, speed, attack_range):
        self.image = load_image("archer.png")
        super().__init__(group, health, strength, defence, speed, attack_range, self.image)


class Barbarian(Hero):
    def __init__(self, group, health, strength, defence, speed, attack_range):
        self.image = load_image("barbarian.png")
        super().__init__(group, health, strength, defence, speed, attack_range, self.image)


class Crusader(Hero):
    def __init__(self, group, health, strength, defence, speed, attack_range):
        self.image = load_image("crusader.png")
        super().__init__(group, health, strength, defence, speed, attack_range, self.image)


class Necromancer(Hero):
    def __init__(self, group, health, strength, defence, speed, attack_range):
        self.image = load_image("necromancer.png")
        super().__init__(group, health, strength, defence, speed, attack_range, self.image)

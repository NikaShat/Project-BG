import pygame, load_image


class Particle(pygame.sprite.Sprite):
    def __init__(self, begin_pos, end_pos, all_sprites):
        super().__init__(all_sprites)
        self.image = load_image.loadimage("partic.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = begin_pos
        self.x, self.y = end_pos

    def update(self, tiles_group_not_collide):
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(tiles_group_not_collide):
            self.kill()

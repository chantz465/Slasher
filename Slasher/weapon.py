import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self,player,groups):
        super().__init__()
        direction = player.status.split('_')



        # graphic
        self.image = pygame.Surface((40,40))

        # placement
        self.rect = self.image.get_rect(center = player.rect.center)
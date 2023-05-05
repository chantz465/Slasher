import pygame
from setting import *

class Level:
    def __init__(self):
        # get the dispaly surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row in WORLD_MAP:
            print(row)

    def run(self):
        # update and draw the game
        pass



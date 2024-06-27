import pygame

from projectsettings import *

class Tiles(pygame.sprite.Sprite):
    def __init__(self, pos, groups, type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        
        #sprite type
        self.spriteType = type
        #spriteimg
        self.image = surface
        # self.image = pygame.image.load('../assets/Palette.png').convert_alpha()
        #sprite collision
        if self.spriteType == 'objects':
            self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - TILESIZE))
            self.hitbox = self.rect.inflate(-6, -20)
        else:
            self.rect = self.image.get_rect(topleft = pos)
            #sprite modified collision
            self.hitbox = self.rect.inflate(-6, -10)
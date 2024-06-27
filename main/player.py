import pygame
from projectsettings import *

# onebyroot2 = 0.707

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obs_sprites):
        super().__init__(groups)
        
        self.obs_sprites = obs_sprites
        
        #spriteimg
        self.image = pygame.image.load('graphics/test/cat.png').convert_alpha()
        #sprite collision/ actual boundary of the sprite
        self.rect = self.image.get_rect(topleft = pos)
        #sprite modified collision
        self.hitbox = self.rect.inflate(-20, -45)
        
        #movement direciton vector
        self.movement = pygame.math.Vector2()
        self.speed = 15
        
    def input(self):
        keyspressed = pygame.key.get_pressed()
        
        if keyspressed[pygame.K_w]:
            self.movement.y = -1
        elif keyspressed[pygame.K_s]:
            self.movement.y = 1
        else:
            self.movement.y = 0
            
        if keyspressed[pygame.K_a]:
            self.movement.x = -1
        elif keyspressed[pygame.K_d]:
            self.movement.x = 1
        else:
            self.movement.x = 0
        
        # if self.movement.x and self.movement.y:
        #     self.movement.x *= onebyroot2
        #     self.movement.y *= onebyroot2
            
    def move(self, speed):
        if self.movement.magnitude() != 0:
            self.movement = self.movement.normalize()
            
            self.hitbox.x += self.movement.x * speed
            self.collision('hori')
            self.hitbox.y += self.movement.y * speed
            self.collision('verti')
            self.rect.center = self.hitbox.center
        # self.rect.center += self.movement * speed
        
    def collision(self, dir):
        if dir == 'hori':
            for sprites in self.obs_sprites:
                if self.hitbox.colliderect(sprites.hitbox):
                    if self.movement.x > 0:
                        self.hitbox.right = sprites.hitbox.left
                    elif self.movement.x < 0:
                        self.hitbox.left = sprites.hitbox.right
        
        if dir == 'verti':
            for sprites in self.obs_sprites:
                if self.hitbox.colliderect(sprites.hitbox):
                    if self.movement.y > 0:
                        self.hitbox.bottom = sprites.hitbox.top
                    elif self.movement.y < 0:
                        self.hitbox.top = sprites.hitbox.bottom
            
    def update(self):
        self.input()
        self.move(self.speed)
        
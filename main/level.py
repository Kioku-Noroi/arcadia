import pygame
from projectsettings import *
from tile import Tiles
from player import Player
from supportingfunctions import *
from random import choice

class Level:
    def __init__(self) -> None:
        #gets the dispaly surfface
        self.displaySurface = pygame.display.get_surface()
        
        #grouping sprites        
        self.Vis_sprites = YCameraGroup()
        self.Obs_sprites = pygame.sprite.Group()
        
        #map
        self.createMap()
        
    def createMap(self):
        
        #map layout dictionary(style and map data)
        layouts = {
            'blockTILE': importCSV('map/csv/map_floorblock.csv'),
            'grassTILE': importCSV('map/csv/map_grass.csv'),
            'objectTILE': importCSV('map/csv/map_OBJECTS.csv'),
        }
        graphics = {
            'grass': importFolder('graphics/grass'),
            'objects': importFolder('graphics/objects')
        }
        for style, mapdata in layouts.items():
            for rowCount, row in enumerate(mapdata):
                for columnCount, column in enumerate(row):
                    # print(column)
                    if column != '-1':
                        x = columnCount * TILESIZE
                        y = rowCount * TILESIZE
                        if style == 'blockTILE':
                            Tiles((x,y), [self.Obs_sprites], 'invisible')
                        if style == 'grassTILE':
                            chosengrass = choice(graphics['grass'])
                            Tiles((x,y), [self.Vis_sprites, self.Obs_sprites], 'grass', chosengrass)
                        if style == 'objectTILE':
                            imgsurf = graphics['objects'][int(column)]
                            print(int(column))
                            Tiles((x,y), [self.Vis_sprites, self.Obs_sprites], 'objects', imgsurf)                    
                    # if column == 'x':
                    #     self.t = Tiles((x,y), [self.Vis_sprites, self.Obs_sprites])
                    # if column == 'p':
                    #     self.p = Player((x,y), [self.Vis_sprites], self.Obs_sprites)
        
        
                    
                    
        self.p = Player((2000,1600), [self.Vis_sprites], self.Obs_sprites)
        
        
    def run(self):
        self.Vis_sprites.newDraw(self.p)
        self.Vis_sprites.update()
        # print(self.p.movement)
        # for x in self.p.movement:
        #     print(x)
        
        
class YCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.displaySurface = pygame.display.get_surface()
        
        #base floor
        self.floorSurf = pygame.image.load('graphics/tilemap/mainground.png')
        self.floorRect = self.floorSurf.get_rect(topleft = (0, 0))
        
        
        self.offset = pygame.math.Vector2()
        
        
    def newDraw(self, playeR):
        self.offset.x = -(playeR.rect.centerx - WINDOWWIDTH // 2)
        self.offset.y = -(playeR.rect.centery - WINDOWHEIGHT // 2)
        
        self.displaySurface.blit(self.floorSurf, self.floorRect.topleft + self.offset)
        
        for sprite in sorted(self.sprites(), key = lambda sprite : sprite.rect.centery):
            self.displaySurface.blit(sprite.image, sprite.rect.topleft + self.offset)
import pygame
from csv import reader as rd
from os import walk

def importCSV(filepath):
    maplayout = []
    with open(filepath) as mapdata:
        csvlayout = rd(mapdata, delimiter = ',')
        for row in csvlayout:
            # print(row)
            maplayout.append(list(row))
        return maplayout
    
def importFolder(path):
    imageSurfaceList = []
    for _, __, data in walk(path):
        for img_name in data:
            imageSurface = pygame.image.load(path + '/' + img_name).convert_alpha()
            imageSurfaceList.append(imageSurface)
        return imageSurfaceList
    
# print(importCSV('map/csv/map_floorblock.csv'))

# print(importFolder('graphics/grass'))
import pygame
from sys import exit

from level import Level
from projectsettings import *

class Game:
    def __init__(self):
        pygame.init()
        self.gof = 2
        self.sc = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        pygame.display.set_caption('arc')
        self.clock = pygame.time.Clock()
        self.level = Level()
        
    def gameRun(self):
        while True:
            for event in pygame.event.get():
                keypressed = pygame.key.get_pressed()
                if event.type == pygame.QUIT or keypressed[pygame.K_ESCAPE]:
                    pygame.display.quit()
                    pygame.quit()
                    exit()
            self.sc.fill('Black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
        
        
if __name__ == '__main__':
    newGame = Game()
    newGame.gameRun()
import pygame
import sys

from setup import *
from support import load_image, load_images

from background import BackGround

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dragon Running")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.assets = {
            'bg': load_image('bg1.png'),
            'dino': load_images('dino'),
        }
        
        self.bg = [BackGround(0, self.assets['bg']), BackGround(WIDTH, self.assets['bg'])]
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            for bg in self.bg:
                bg.update()
                bg.render(self.screen)
            self.clock.tick(FPS)
            pygame.display.update()

game = Game()
game.run()
import pygame
import sys

from setup import *
from support import load_image, load_images

from background import BackGround
from dino import Dino


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

        self.bg = [BackGround(0, self.assets['bg']),
                   BackGround(WIDTH, self.assets['bg'])]
        self.dino = Dino(self, (10, HEIGHT - HEIGHT / 3 - 4), (44, 44))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dino.velocity[1] = -7

            for bg in self.bg:
                bg.update()
                bg.render(self.screen)

            self.dino.update()
            self.dino.render(self.screen)
            self.clock.tick(FPS)
            pygame.display.update()


game = Game()
game.run()

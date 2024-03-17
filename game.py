import pygame
import sys
import random

from setup import *
from support import load_image, load_images

from background import BackGround
from dino import Dino
from cactus import Cactus


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dragon Running")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.assets = {
            'bg': load_image('bg1.png'),
            'cactus': load_image('cactus.png'),
            'dino': load_images('dino'),
        }

        self.bg = [BackGround(0, self.assets['bg']),
                   BackGround(WIDTH, self.assets['bg'])]
        self.dino = Dino(self, (20, HEIGHT - HEIGHT / 3), (44, 44))
        self.cactus = Cactus(
            self, (WIDTH + 160, HEIGHT - HEIGHT / 3 - 20), (70, 130))
        self.obstacles = []

    def run(self):
        while True:
            for cactus in self.obstacles:
                if cactus.pos[0] < -WIDTH:
                    self.obstacles.remove(cactus)
                cactus.update()
                cactus.render(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.dino.velocity[1] = -13
                    if event.key == pygame.K_DOWN:
                        self.dino.velocity[1] = 9999999

            if random.random() * 5000 < 50:
                self.obstacles.append(
                    Cactus(self, (WIDTH, HEIGHT - HEIGHT / 3 - 20), (70, 130)))

            for bg in self.bg:
                bg.update()
                bg.render(self.screen)

            self.dino.update()
            self.dino.render(self.screen)

            for cactus in self.obstacles:
                if cactus.pos[0] < -WIDTH:
                    self.obstacles.remove(cactus)
                cactus.update()
                cactus.render(self.screen)

            self.clock.tick(FPS)
            pygame.display.update()


game = Game()
game.run()

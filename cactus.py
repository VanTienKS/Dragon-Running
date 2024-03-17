import pygame
from setup import *


class Cactus:
    def __init__(self, game, pos, size, speed=8):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.speed = speed

    def update(self):
        self.pos[0] -= self.speed
    
    def render(self, screen):
        screen.blit(pygame.transform.scale(
            self.game.assets['cactus'], self.size), self.pos)

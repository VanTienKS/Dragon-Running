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
        
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def render(self, screen):
        screen.blit(pygame.transform.scale(
            self.game.assets['cactus'], self.size), self.pos)

import pygame
from setup import *


class Dino:
    def __init__(self, game, pos, size, img_duration=6):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.frame = 0
        self.img_duration = img_duration
        self.velocity = [0, 0]
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, obstacles):
        
        dino_rect = self.rect()
        for cactus in obstacles:
            if dino_rect.colliderect(cactus.rect()):
                self.game.playing = False
        
        self.frame = (self.frame + 1)
        if self.frame >= len(self.game.assets['dino']) * self.img_duration:
            self.frame = 0

        self.velocity[1] = min(8, self.velocity[1]+0.4)
        self.pos[1] += self.velocity[1]
        if self.pos[1] > (HEIGHT - HEIGHT / 3 + 20):
            self.pos[1] = (HEIGHT - HEIGHT / 3 + 20)
            self.velocity[1] = 0

    def render(self, screen):
        screen.blit(self.game.assets['dino']
                    [self.frame // self.img_duration], self.pos)

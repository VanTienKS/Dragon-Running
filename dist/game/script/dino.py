import pygame
import os
from setup import *


class Dino:
    def __init__(self, game, pos, size, img_duration=6):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.frame = 0
        self.img_duration = img_duration
        self.velocity = [0, 0]
        self.collition_down = False
        self.set_sound()

    def set_sound(self):
        jump_path = os.path.join('assets\\sounds\\jump.wav')
        die_path = os.path.join('assets\\sounds\\die.wav')
        self.jump_sound = pygame.mixer.Sound(jump_path)
        self.die_sound = pygame.mixer.Sound(die_path)

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, obstacles):
        self.collition_down = False
        dino_rect = self.rect()
        for cactus in obstacles:
            if dino_rect.colliderect(cactus.rect()):
                self.die_sound.play()
                self.game.playing = False
                

        self.frame = (self.frame + 1)
        if self.frame >= len(self.game.assets['dino']) * self.img_duration:
            self.frame = 0

        self.velocity[1] = min(10, self.velocity[1]+0.4)
        self.pos[1] += self.velocity[1]
        if self.pos[1] > (HEIGHT - HEIGHT / 3 + 20):
            self.pos[1] = (HEIGHT - HEIGHT / 3 + 20)
            self.velocity[1] = 0
            self.collition_down = True

    def jump(self):
        if self.collition_down:
            self.jump_sound.play()
            self.velocity[1] = -13

    def render(self, screen):
        screen.blit(self.game.assets['dino']
                    [self.frame // self.img_duration], self.pos)

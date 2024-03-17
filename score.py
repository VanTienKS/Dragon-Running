import pygame
from setup import *


class Score:
    def __init__(self, max_score=0, curent_score=0):
        self.max_score = max_score
        self.curent_score = curent_score
        self.font = pygame.font.SysFont('monospace', 45)
        self.color = (0, 0, 0)
        self.time = 0

    def set_label(self, screen):
        big_font = pygame.font.SysFont('monospace', 48, bold=True)
        small_font = pygame.font.SysFont('monospace', 32)
        self.big_label = big_font.render(f'G A M E  O V E R', 1, (0, 0, 0))
        self.small_font = small_font.render(
            f'press r to restart', 1, (0, 0, 0))
        screen.blit(self.big_label, (WIDTH // 2 -
                    self.big_label.get_width() // 2, HEIGHT // 4))
        screen.blit(self.small_font, (WIDTH // 2 -
                    self.small_font.get_width() // 2, HEIGHT // 2))

    def update(self):
        self.time += 1
        self.curent_score = int(self.time / 8)
        self.max_score = self.curent_score if self.curent_score > self.max_score else self.max_score

    def render(self, screen):
        self.label = self.font.render(f"Score   {self.max_score}  {
                                      self.curent_score}", 1, self.color)
        label_width = self.label.get_rect().width
        screen.blit(self.label, (WIDTH - label_width - 10, 10))

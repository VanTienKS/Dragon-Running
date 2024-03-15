from setup import *


class Dino:
    def __init__(self, game, pos, size, img_duration=6):
        self.game = game
        self.pos = list(pos)
        self.size = size
        self.frame = 0
        self.img_duration = img_duration
        self.velocity = [0, 0]

    def update(self):
        self.frame = (self.frame + 1)
        if self.frame >= len(self.game.assets['dino']) * self.img_duration:
            self.frame = 0

        self.velocity[1] = min(5, self.velocity[1]+0.2)
        self.pos[1] += self.velocity[1]
        if self.pos[1] > (HEIGHT - HEIGHT / 3 - 4):
            self.pos[1] = (HEIGHT - HEIGHT / 3 - 4)
            self.velocity[1] = 0

    def render(self, screen):
        screen.blit(self.game.assets['dino']
                    [self.frame // self.img_duration], self.pos)

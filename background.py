from setup import WIDTH
class BackGround:
    def __init__(self, x, img):
        self.img = img
        self.x = x
        self.speed = 5
        
    def update(self):
        self.x -= self.speed
        if self.x <= -WIDTH+10:
            self.x = WIDTH
            
    def render(self, screen):
        screen.blit(self.img, (self.x, 0))
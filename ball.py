import pygame
import random

white = (255, 255, 255)
black = (0, 0, 0)

class Ball:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = 345.0
        self.y = 420.0
        self.vel_x = random.randrange(4, 10)
        ch = random.randrange(0,1)
        if ch == 0:
            self.vel_x *= -1
        self.vel_y = random.randrange(-10, 10)
        if self.vel_y == 0:
            self.vel_y += 1
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(white)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        if self.y <= 30:
            self.vel_y *= -1
        if self.y >= 690:
            self.vel_y *= -1
        
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self, win):
        win.blit(self.surf, (self.x, self.y))

    
    def get_mask(self):
        return pygame.mask.from_surface(self.surf)

    def out_of_bounds(self):
        # print(self.x)
        if self.x < 0 or self.x > 700:
            return True

    def hit(self):
        self.vel_x *= -1.1
        if self.vel_x >= 12:
            self.vel_x = 12
            
        self.vel_y *= 1.1

        if self.vel_y >= 12:
            self.vel_y = 12
        

     
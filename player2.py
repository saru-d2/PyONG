import pygame
import random
from ball import *
from random import randint

white = (255, 255, 255)
black = (0, 0, 0)


class Player2:
    def __init__(self):
        self.score = 0
        self.killed = False
        self.vel = 20
        self.x = 650.0
        self.y = random.randrange(30.0, 600)
        self.height = 100
        self.width = 20
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((randint(0,255), randint(0, 255), randint(0, 255)))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(self.surf, (self.x, self.y))

    def up(self):
        if self.y > self.vel:
            self.y -= self.vel
        else:
            self.y = 0

    def down(self):
        if self.y + self.height < 700:
            self.y += self.vel
        else:
            self.y = 600

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def collide_ball(self, ball):
        if ball.y + ball.height - self.y >= 0 and self.y + self.height - ball.y >= 0:
            if abs(self.x  - (ball.x + ball.width)) <= abs(ball.vel_x) :
                return True

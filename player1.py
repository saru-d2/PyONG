import pygame
import random

white = (255, 255, 255)
black = (0, 0, 0)

class Player1:
    def __init__(self):
        self.score = 0
        self.vel = 20
        self.x = 30
        # self.y = random.randrange(30, 600)
        # self.height = 100
        self.y = 0
        self.height = 700
        self.width = 20
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill(white)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(self.surf, (self.x, self.y))

    def up(self):
        self.y -= self.vel

    def down(self):
        self.y += self.vel

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    
    def collide_ball(self, ball):
        r = self.get_rect()
        if ball.y + ball.height - self.y >= 0 and self.y + self.height - ball.y >= 0:
            if self.x + self.width - ball.x >= 0 and ball.x + ball.width - self.x >= 0:
                return True

    # def collide_ball(self, ball):
    #     r = self.get_rect()
    #     if ball.y + ball.height - self.y >= 0 and self.y + self.height - ball.y >= 0:
    #         if abs(self.x + self.width  - (ball.x + ball.width)) <= ball.vel_x :
    #             return True

    # def collide_ball(self, ball):
    #     r = self.get_rect()
    #     if abs(self.x + self.width  - (ball.x )) <= ball.vel_x :
    #         return True
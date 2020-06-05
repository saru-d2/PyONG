import pygame
from draw_win import *
from player1 import *
from player2 import *
from ball import *
from collide import *

def main():
    clock = pygame.time.Clock()
    p1 = Player1()
    p2 = Player2()
    balls = []
    balls.append(Ball())
    run = True
    while run == True:
        ball = balls[-1]

        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            p1.up()
        if keys[pygame.K_s]:
            p1.down()
        if keys[pygame.K_UP]:
            p2.up()
        if keys[pygame.K_DOWN]:
            p2.down()
        
        if p1.collide_ball(ball):
            print("hit 1")
            ball.hit()

        if p2.collide_ball(ball):
            print("hit 2")
            ball.hit()

        if ball.out_of_bounds():
            if ball.x < 0:
                p2.score += 1
            else:
                p1.score += 1
            balls.append(Ball())

        ball.update()
        p2s = [p2]
        draw_win(p1, p2s, ball)
main()


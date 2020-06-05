import pygame
pygame.font.init()


white = (255, 255, 255)
black = (0,0,0)
win = pygame.display.set_mode((700, 700))
bg = pygame.Surface((700, 700))
bg.fill(black)

font = pygame.font.SysFont("comicsans", 30)


def draw_win(p1, p2s, ball):
    if len(p2s) <=0 :
        return

    win.blit(bg, (0,0))
    p1.draw(win)
    for p2 in p2s:
        p2.draw(win)
    ball.draw(win)
    score1 = font.render("P1: " + str(p1.score), 1, white)
    score2 = font.render("P2: " + str(p2s[0].score), 1, white)
    win.blit(score1, (5,30))
    win.blit(score2, (500, 30))
    ball_coor = font.render(str(ball.x) + ", " + str(ball.y), 1, white)
    win.blit(ball_coor, (250, 30))
    pygame.display.update()


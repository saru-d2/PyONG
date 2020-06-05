import pygame
from player1 import *
from player2 import *
from ball import *

def collide_p1( p1, ball):
    p1_mask = p1.get_mask()
    ball_mask = ball.get_mask()
    offset = ( ball.x - p1.x , ball.y - p1.y)
    if p1_mask.overlap(ball_mask, offset):
        ball.vel_y *= -1
        return True


def collide_p2( p2, ball):
    p2_mask = p2.get_mask()
    ball_mask = ball.get_mask()

    offset = ( ball.x - p2.x , ball.y - p2.y)
    if p2_mask.overlap(ball_mask, offset):
        ball.vel_y *= -1
        return True
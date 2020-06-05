import pygame
from draw_win import *
from player1 import *
from player2 import *
from ball import *
from collide import *
import neat
import os


def main(genomes, config):
    print("gen")
    clock = pygame.time.Clock()
    p1 = Player1()
    p2s = []
    nets = []
    ge = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        p2s.append(Player2())
        g.fitness = 0
        ge.append(g)

    # p2 = Player2()
    balls = []
    balls.append(Ball())
    run = True
    noNotHit = 0

    while run == True:
        if len(p2s) <= 0 :
            run = False
            break
        # print(ge[0].fitness)

        ball = balls[-1]

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            p1.up()
        if keys[pygame.K_s]:
            p1.down()
        # if keys[pygame.K_UP]:
        #     p2.up()
        # if keys[pygame.K_DOWN]:
        #     p2.down()

        for i, p2 in enumerate(p2s):
            ge[i].fitness += 0.1
            output = nets[i].activate((
                p2.y, abs(ball.y - p2.y), abs(ball.y -(p2.y + p2.height)), ball.x))
            if output[0] > 0.5:
                p2.up()
            if output[1] > 0.5:
                p2.down()

            pass

        if ball.x < 40 and ball.vel_x <0 : 
            ball.hit()

        
        
            

        # print(str (abs(p2s[0].x  - (ball.x + ball.width))) + "    "+str(ball.vel_x))
        if len(p2s) <= 0:
            run = False
            break
        # if len(p2s) > 0:
        li = []
        if abs(p2s[0].x - (ball.x + ball.width)) <= abs(ball.vel_x) :
            n = 0
            for i, p2 in enumerate(p2s) : 
                if not p2.collide_ball(ball):
                    n += 1
                    li.append(i)
                    p2.killed = True
            print("   n: " + str(n))
        
        for i, p2 in enumerate(p2s):
            if p2.killed : 
                ge[i].fitness -= 1
                p2s.pop(i)
                ge.pop(i)
                nets.pop(i)
            
          
        
        for i, p2 in enumerate(p2s):
            if p2.killed:
                p2s.pop(i)
                nets.pop(i)
                ge.pop(i)
            if p2.collide_ball(ball):
                # print("hit 2")
                ball.hit()
                break

        if ball.out_of_bounds():
            if ball.x < 0:
                p2s[0].score += 1
                for g in ge:
                    g.fitness += 5
            else:
                p1.score += 1
            balls.append(Ball())

        ball.update()
        if len(p2s) > 0:
            draw_win(p1, p2s, ball)


# main()


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(main, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)

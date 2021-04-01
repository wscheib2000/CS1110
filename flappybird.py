# Will Scheib wms9gv
"""
Creates a Flappy Bird game.
"""

import gamebox
import pygame
import random

COUNTER = 0
SCORE = 0
LOSS = 0
bird = gamebox.from_color(100, 200, "yellow", 40, 40)
bird.xspeed = 5
camera = gamebox.Camera(800, 600)
pipes = []


def tick(keys):
    global COUNTER, SCORE, LOSS

    if pygame.K_SPACE in keys:
        bird.yspeed = -15

    bird.move_speed()
    if bird.y > 580:
        bird.y = 580
        LOSS = 1
    bird.yspeed += 2
    camera.clear("cyan")
    camera.draw(bird)

    camera.x += 5

    COUNTER += 1
    if COUNTER % 100 == 0:
        midpoint = random.randint(200, 400)
        new_pipe_top = gamebox.from_color(camera.x + 450, (midpoint - 150)/2, "green", 50, midpoint - 150)
        new_pipe_bottom = gamebox.from_color(camera.x + 450, ((600 - (midpoint + 150)) / 2) + (midpoint + 150), "green",
                                             50, 600 - midpoint + 150)
        pipes.append(new_pipe_top)
        pipes.append(new_pipe_bottom)
    for pipe in pipes:
        if pipe.x < camera.x - 450:
            pipes.remove(pipe)
        else:
            camera.draw(pipe)
        if pipe.x - bird.x == -5:
            SCORE += .5
        if bird.touches(pipe):
            LOSS = 1
        if pipe.x - bird.x <= 25 and bird.y < 0:
            LOSS = 1

    camera.draw(gamebox.from_text(camera.x, 100, str(int(SCORE)), 150, "white", bold=True))
    if LOSS == 1:
        gamebox.pause()
        # Got try/except statement from https://stackoverflow.com/questions/35807605/create-a-file-if-it-doesnt-exist
        try:
            best_scores_file = open("flappy_best.txt", 'r')
            best_score = best_scores_file.readline()
            best_scores_file.close()
            if len(best_score) == 0 or int(best_score) < SCORE:
                best_scores_file = open("flappy_best.txt", "w")
                best_scores_file.write(str(int(SCORE)))
                best_score = str(int(SCORE))
        except IOError:
            best_scores_file = open("flappy_best.txt", "w")
            best_scores_file.write(str(int(SCORE)))
            best_score = str(int(SCORE))

        camera.clear("cyan")
        camera.draw(bird)
        for pipe in pipes:
            camera.draw(pipe)
        camera.draw(gamebox.from_text(camera.x, 150, "GAME OVER", 75, "gold", bold=True))
        camera.draw(gamebox.from_color(camera.x, 300, "beige", 400, 150))
        camera.draw(gamebox.from_text(camera.x - 75, 265, "SCORE", 50, "black", bold=True))
        camera.draw(gamebox.from_text(camera.x - 75, 335, "BEST", 50, "black", bold=True))
        camera.draw(gamebox.from_text(camera.x + 100, 265, str(int(SCORE)), 50, "black", bold=True))
        camera.draw(gamebox.from_text(camera.x + 100, 335, best_score, 50, "black", bold=True))
    camera.display()


ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

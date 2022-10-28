import pygame
from pygame.draw import circle, rect
from random import randint
import numpy as np


def Catch_The_Ball(a, b):
    '''Starts the game with 'a' number of circles and 'b' number of squares. Circles trajectory is a straight line, but
    they bounce off of the edge of screen. Trajectory of each of the square is a circumference. By clicking on a circle
    you get 1 point, by clicking on a square you get 3 points.'''

    pygame.init()

    FPS = 120                                                                                                           # Setting FPS to 120
    screen = pygame.display.set_mode((1200, 900))

    RED = (255, 0, 0)                                                                                                   # Creating the list of all the
    BLUE = (0, 0, 255)                                                                                                  # possible circles and squares
    YELLOW = (255, 255, 0)                                                                                              # colors
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

    def speed():
        '''Generates random values, which will be used as x and y projections of balls speed.'''
        x_speed = randint(-500, 500)/100
        y_speed = randint(-500, 500)/100
        return [x_speed, y_speed]

    def omega_gen():
        '''Generates random value, which will be used as angular velocity of squares speed.'''
        return randint(-1000, 1000)/50000

    def new_ball():
        '''Generates a new circle and returns its coordinates, radius and color.'''
        x = randint(100, 1100)
        y = randint(100, 800)
        r = randint(10, 100)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)
        return [x, y, r, color]

    def new_square():
        '''Generates a new square and returns its parametrs. X, Y and R are coordinates and radius of the
        curcumference, which is the trajectory of square's left corner. Theta is an angle of orientation of R, counting
        counterclockwise from the vertical. r is lenth of the square.'''
        color = COLORS[randint(0, 5)]
        X = randint(200, 1000)
        Y = randint(200, 700)
        R = randint(0, 400)
        Theta = randint(0, 10000)
        r = randint(10, 100)
        rect(screen, color, (X + R*np.sin(Theta), Y + R * np.cos(Theta), r, r))
        return [color, X, Y, R, Theta, r]

    def ball(positions):
        '''Draws a circle.
        Takes the list of its x, y, r and color as an input.'''
        x = positions[0]
        y = positions[1]
        r = positions[2]
        color = positions[3]
        circle(screen, color, (x, y), r)

    def square(possqare):
        '''Draws a square.
        Takes the list of its color, X, Y, R, Theta, r, which where defined in new_square function'''
        x = possqare[1] + possqare[3]*np.sin(possqare[4])
        y = possqare[2] + possqare[3]*np.cos(possqare[4])
        r = possqare[5]
        color = possqare[0]
        rect(screen, color, (x, y, r, r))

    def score_display(font_size):
        '''Displays your current score. Takes font size as an argument'''
        myfont = pygame.font.SysFont("monospace", font_size)
        scoretext = myfont.render("Score = " + str(score), 1, (255, 255, 255))
        screen.blit(scoretext, (5, 10))

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    score = 0                                                                                                           # Setting initial score to 0

    positions = []                                                                                                      # Creating initial circles and
    speed_list = []                                                                                                     # lists whith their parametrs
    for i in range(a):
        positions.append(new_ball())
        speed_list.append(speed())

    omega = []                                                                                                          # Creating initial squares and
    possqare = []                                                                                                       # lists whith their parametrs
    for i in range(b):
        possqare.append(new_square())
        omega.append(omega_gen())

    while not finished:
        clock.tick(FPS)

        screen.fill(BLACK)                                                                                              # Deletes all the figures
                                                                                                                        # from the screen

        for i in range(len(possqare)):                                                                                  # Rotates the R vector from the
            possqare[i][4] = possqare[i][4] + omega[i]                                                                  # center of the trajectory of
                                                                                                                        # each square to its left corner

        for i, pos in enumerate(positions):
            positions[i][0] = positions[i][0] + speed_list[i][0]                                                        # Moves each circle
            positions[i][1] = positions[i][1] + speed_list[i][1]

            if positions[i][0] + positions[i][2] >= 1200 or positions[i][0] - positions[i][2] <= 0:                     # Checks, if any part of the circle
                speed_list[i][0] = -speed_list[i][0]                                                                    # is out of bounds. If it is,
            if positions[i][1] + positions[i][2] >= 900 or positions[i][1] - positions[i][2] <= 0:                      # changes its x or y velocity to
                speed_list[i][1] = -speed_list[i][1]                                                                    # the opposite one, so that the
                                                                                                                        # circle will return from out of
                                                                                                                        # bounds

        for i in range(len(possqare)):                                                                                  # Draws a moving square
            square(possqare[i])

        for i in range(len(positions)):                                                                                 # Draws a moving circle
            ball(positions[i])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, position in enumerate(positions):                                                                # Checks, if click was inside a
                    if (event.pos[0]-position[0])**2 + (event.pos[1]-position[1])**2 <= position[2]**2:                 # circle. If it was, pops the circle,
                        score += 1                                                                                      # creates a new one with new parametrs
                        positions[i] = new_ball()                                                                       # and raises the score number by 1
                        speed_list[i] = speed()
                for i, position in enumerate(possqare):                                                                 # Checks, if click was inside a
                    if  abs(event.pos[0]-position[1] - position[3]*np.sin(position[4])-0.5*position[5]) \
                    <= 0.5*position[5] and \
                    abs(event.pos[1] -position[2] - position[3]*np.cos(position[4]) - 0.5 * position[5]) \
                    <=  0.5*position[5]:                                                                                # square. If it was, pops the square,
                        score += 3                                                                                      # creates a new one with new parametrs
                        possqare[i] = new_square()                                                                      # and raises the score number by 3
                        omega[i] = omega_gen()

        score_display(25)

        pygame.display.update()

    pygame.quit()


Catch_The_Ball(2, 3)
import pygame
from pygame.draw import circle, rect, polygon

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (220, 220, 220), (0, 0, 500, 500))                                                                         # Making the background gray

circle(screen, (255, 255, 0), (250, 250), 125)                                                                          # Drawing face

circle(screen, (255, 0, 0), (305, 225), 18)                                                                             # Drawing eyes
circle(screen, (255, 0, 0), (195, 225), 23)

circle(screen, (0, 0, 0), (305, 225), 9)                                                                                # Drawing pupils
circle(screen, (0, 0, 0), (195, 225), 11)

rect(screen, (0, 0, 0), (195, 320, 115, 23))                                                                            # Drawing mouth

polygon(screen, (0, 0, 0), ((125, 145), (135, 140),                                                                     # Drawing eyebrows using polygons
                            (230, 206), (220, 216)))
polygon(screen, (0, 0, 0), ((275, 215), (400, 172),
                            (395, 162), (270, 205)))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
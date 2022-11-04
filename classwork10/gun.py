import math
from random import choice
import random as rnd

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface):
        """Constructor of Ball class
        Creates initial coordinates, color and lifetime parametr of the ball
        """
        self.screen = screen
        self.x = gun.x
        self.y = gun.y
        self.r = 10
        self.color = choice(GAME_COLORS)
        self.tick = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        # Fixed
        self.vy = self.vy - 3
        if self.y + self.r >= 600 or self.y - self.r <= 0:
            self.vy = -self.vy * 0.6
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx = -self.vx * 0.6
        if self.x + self.r >= 800:
            self.x = self.x - abs(self.vx)
        if self.x - self.r <= 0:
            self.x = self.x + abs(self.vx)
        if self.y + self.r >= 600:
            self.y = self.y - abs(self.vy)
        if self.y - self.r <= 0:
            self.y = self.y + abs(self.vy)
        self.tick += 1


    def draw(self):
        '''Draws a ball'''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXED
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        '''Creates coordinates, color and power parametrs of the gun'''
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20
        self.y = 450

    def fire2_start(self):
        '''Enables the charging mode of the gun'''
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0]-self.x > 0:
                self.an = math.atan((event.pos[1]-self.y) / (event.pos[0]-self.x))
            elif event.pos[0]-self.x < 0:
                self.an = +math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x)) + math.pi
            else:
                if event.pos[1]-self.y <=0:
                    self.an = math.asin(-1)
                else:
                    self.an = math.asin(1)
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        '''Draws the gun'''
        pygame.draw.line(
            self.screen,
            self.color,
            (self.x, self.y),
            (self.x + math.cos(self.an) * (15 + self.f2_power/2), self.y + math.sin(self.an)
             * (15 + self.f2_power/2)),
            width = 7
        )

    def power_up(self):
        '''Charges the gun'''
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def moveleft(self):
        '''Moves the gun left'''
        if self.x > 0:
            self.x = self.x - 1

    def movedown(self):
        '''Moves the gun down'''
        if self.y < 600:
            self.y = self.y + 1

    def moveright(self):
        '''Moves the gun right'''
        if self.x < 800:
            self.x = self.x + 1

    def moveup(self):
        '''Moves the gun up'''
        if self.y > 0:
            self.y = self.y - 1


class Target:
    def __init__(self, screen):
        '''Creates coordinates, parametrs and score points, which correspond to this target'''
        self.screen = screen
        self.points = 0
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd.randint(60, 740)
        self.y = rnd.randint(60, 540)
        self.r = rnd.randint(2, 50)
        self.color = RED
        self.vx = rnd.randint(-100, 100)/10
        self.vy = rnd.randint(-100, 100)/10

    def hit(self, points=1):
        '''Score goes up by 1 when hitting the target'''
        self.points += points

    def draw(self):
        '''Draws the target'''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def move(self):
        '''Moves the target'''
        self.x += self.vx
        self.y -= self.vy
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx = -self.vx
        if self.y + self.r >= 600 or self.y - self.r <= 0:
            self.vy = -self.vy


pygame.init()                                                                                                           # Initializing pygame stuff
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

balls = []                                                                                                              # Creating list of all the balls

clock = pygame.time.Clock()
gun = Gun(screen)                                                                                                       # Creating gun and two targets
target1 = Target(screen)
target2 = Target(screen)
targets = [target1, target2]                                                                                            # Creating list of all targets

Akey, Skey, Dkey, Wkey = False, False, False, False                                                                     # I will need those in 260 line of code

textfont = pygame.font.SysFont('monospace', 27)                                                                         # Font for the score counter

finished = False

while not finished:

    screen.fill(WHITE)

    score = target1.points + target2.points

    gun.draw()
    target1.draw()
    target2.draw()
    for b in balls:
        b.draw()
        if b.tick >= 100:                                                                                               # Destroing balls if their lifetime has expired
            balls.remove(b)

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:                                                                      # Targetting and charging up the gun
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:                                                                                 # I use those 4 parametrs to make the motion of
                Akey = True                                                                                             # the gun continous
            if event.key == pygame.K_s:
                Skey = True
            if event.key == pygame.K_d:
                Dkey = True
            if event.key == pygame.K_w:
                Wkey = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Akey = False
            if event.key == pygame.K_s:
                Skey = False
            if event.key == pygame.K_d:
                Dkey = False
            if event.key == pygame.K_w:
                Wkey = False

    if Akey:
        gun.moveleft()
    if Skey:
        gun.movedown()
    if Dkey:
        gun.moveright()
    if Wkey:
        gun.moveup()

    for target in targets:
        target.move()

    for b in balls:
        b.move()
        for target in targets:
            if b.hittest(target):                                                                                       # Checking if any ball hits a target
                target.hit()
                target.new_target()

    gun.power_up()

    textTBD = textfont.render("Score = " + str(score), 1, (0, 0, 0))                                                    # Displaying score counter
    screen.blit(textTBD, (30, 20))

    pygame.display.update()

pygame.quit()

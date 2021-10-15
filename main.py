import pygame
from Rocket import *
from vector import *
from matrix import *
from population import *
from constants import *
from random import randint
from uiParameters import *
from Obstacles import *
import colorsys
from math import sin

pygame.init()
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Smart Rocket")
clock = pygame.time.Clock()
fps = 60

def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

scale = 40
Distance = 5
speed = 0.03
hue = uniform(0, 2)
temp = hue
lifeSpan = 600
startingPosition = Vector(50, Height//2)
Target = Vector(Width-50, Height//2)

obstacles = []
for i in range(4):
    x = randint(100, Width-100)
    y = randint(100, Height-100)
    w = randint(50, 300)
    h = randint(50, 300)
    o = Obstacle(x, y, w, h)
    obstacles.append(o)

population = Population(screen, Distance, scale, lifeSpan, startingPosition, Target)
population.obstacles = obstacles
population.Initialize()

v = Vector(20, 20)

angle = 0
run = True
while run:
    clock.tick(fps)
    screen.fill((17, 24, 32))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    population.Start()

    pygame.draw.circle(screen, (173, 100, 8), (Target.x, Target.y), 40)
    pygame.draw.circle(screen, (243, 170, 78), (Target.x, Target.y), 40, 5)

    for obstacle in obstacles:
        obstacle.Draw(screen, hsv_to_rgb(hue, 1, 1))
        hue += speed
    hue = temp
    LifeSpan.Render(screen)
    maxFit.Render(screen)
    Generation.Render(screen)
    #pygame.display.update()
    pygame.display.flip()

pygame.quit()

import pygame
from vector import *
from genetic import DNA
from uiParameters import *
import numpy as np
from matrix import *
from math import degrees, radians, pi
from constants import *

def translate(value, min1, max1, min2, max2):
    return min2 + (max2 - min2)* ((value-min1)/(max1-min1))
class Rocket:
    def __init__(self, position = Vector(500, 500), lifeSpan=100, population=None, dna=None):
        self.position = position
        self.velocity = Vector()
        self.acceleration = Vector(0, 0)
        self.lifeSpan = lifeSpan
        self.dna = None
        if dna == None:
            self.dna = DNA(lifeSpan)
        else:
            self.dna = dna
        self.fitness = 0;
        self.angle = 0
        self.color = (255, 255, 255)
        self.secondaryColor = (70, 70, 70)
        self.size = 2
        self.stroke = 2
        self.counter = 0
        self.parent = population
        self.completed = False
        self.crashed = False
    def ApplyForce(self, force):
        self.acceleration = self.acceleration + force

    def Update(self):
        self.ApplyForce(self.dna.genes[self.counter])

        self.counter += 1

        distance = Vector.GetDistance(self.position, self.parent.target)

        if distance < self.parent.targetRadius:
            self.completed = True
            #self.position = self.parent.target

        #check for obstacles
        if self.parent.obstacles != None:
            for obstacle in self.parent.obstacles:
                if (self.position.x > obstacle.position.x and self.position.x < obstacle.position.x + obstacle.width
                and self.position.y > obstacle.position.y and self.position.y < obstacle.position.y + obstacle.height):
                    self.crashed = True

        #check for boundaries
        offset = 5
        if (self.position.x > Width-offset or self.position.x < offset or
        self.position.y > Height - offset or self.position.y < offset):
            self.crashed = True


        self.parent.counter = self.counter
        LifeSpan.text = f"Life Span : {self.counter}/{self.lifeSpan}"

        if self.completed != True and self.crashed != True:
            self.velocity = self.velocity + self.acceleration
            self.position = self.position + self.velocity
            self.acceleration = self.acceleration * 0
            self.angle = self.velocity.Heading() + pi/2

    def CalculateFitness(self):
        distance = Vector.GetDistance(self.position, self.parent.target)
        self.fitness = translate(distance, 0, Width, Width, 0)
        if self.completed == True:
            self.fitness *= 10
        if self.crashed == True:
            self.fitness /= 10


    def Display(self, screen, distance, scale):
        ps = []
        #self.angle = self.velocity.Heading() + pi/2
        points = np.array([ [[0], [-self.size], [0]],
            [[self.size//2], [self.size//2], [0]],
            [[-self.size//2], [self.size//2], [0]]])

        for point in points:
            rotated = np.matmul(rotationZ(self.angle) , point)
            z = 1/(distance - rotated[2][0])
            projection_matrix = np.array([[z, 0, 0],
                                [0, z, 0]])

            projected_2d = np.matmul(projection_matrix, rotated)
            x = int(projected_2d[0][0] * scale) + self.position.x
            y = int(projected_2d[1][0] * scale) + self.position.y
            ps.append((x, y))

        pygame.draw.polygon(screen, self.secondaryColor, ps)
        pygame.draw.polygon(screen, self.color, ps, self.stroke)

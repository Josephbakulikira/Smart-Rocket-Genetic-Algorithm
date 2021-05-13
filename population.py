from Rocket import *
from math import floor
from random import randint, uniform
from uiParameters import *

class Population:
    def __init__(self, screen ,distance, scale, lifeSpan, startPos, target, targetRadius = 40):
        self.rockets = []
        self.population_size = 50
        self.screen = screen
        self.distance = distance
        self.scale = scale
        self.lifeSpan = lifeSpan
        self.startPos = startPos
        self.target = target
        self.targetRadius = targetRadius
        self.matingPool = []
        self.obstacles = None
        self.generations = 1

    def Initialize(self):
        self.rockets = []
        for i in range(self.population_size):
            self.rockets.append(Rocket(self.startPos, self.lifeSpan, self))

    def Evaluate(self):
        maxfit = 0
        #Get the highest fitness of all the rockets
        for rocket in self.rockets:
            rocket.CalculateFitness()
            if rocket.fitness > maxfit:
                maxfit = rocket.fitness
        maxFit.text = f"Fitness: {round(maxfit,2)}"
        for rocket in self.rockets:
            try:
                rocket.fitness /= maxfit
            except ZeroDivisionError:
                print("you can't divide by zero")

        self.matingPool = []
        for i in range(len(self.rockets)):
            n = self.rockets[i].fitness * 100
            for j in range(floor(n)):
                self.matingPool.append(self.rockets[i])

    def NaturalSelection(self):
        newRockets = [Rocket(self.startPos, self.lifeSpan, self) for i in range(self.population_size)]
        if len(self.matingPool) > 0:
            for i in range(len(self.rockets)):
                parentA = self.matingPool[randint(0, len(self.matingPool)-1)].dna
                parentB = self.matingPool[randint(0, len(self.matingPool)-1)].dna

                childDNA =  parentA.crossOver(parentB)
                childDNA.Mutation();
                newRockets[i] = Rocket(self.startPos, self.lifeSpan, self, childDNA)
        self.rockets = newRockets



    def Start(self):
        # counter = 0
        for rocket in self.rockets:
            rocket.Update()
            rocket.Display(self.screen, self.distance, self.scale)
            counter = rocket.counter
            if rocket.counter > self.lifeSpan:
                rocket.counter = 0
        if counter >= self.lifeSpan-1:
            self.generations += 1
            Generation.text = f"Generation: {self.generations}"
            self.Evaluate()
            self.NaturalSelection()

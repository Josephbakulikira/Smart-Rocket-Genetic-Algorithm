from vector import *
from random import randint
from constants import *
class DNA:
    def __init__(self, lifeSpan, Genes=None):
        self.lifeSpan = lifeSpan
        self.genes = [Vector() for i in range(lifeSpan)]
        if Genes == None:
            self.genes = [Vector.RandomVector().SetMagnitude(MaxForce) for i in range(lifeSpan)]
        else:
            self.genes = Genes

    def crossOver(self, partner):
        newGenes = [Vector() for i in range(self.lifeSpan)]
        mid = randint(0, len(self.genes))
        #mid = len(self.genes)//2
        for i in range(len(self.genes)):
            if i>mid:
                newGenes[i] = self.genes[i]
            else:
                newGenes[i] = partner.genes[i]

        return DNA(self.lifeSpan, newGenes)

    def Mutation(self):
        for i in range(len(self.genes)):
            if uniform(0,1) < 0.01:
                self.genes[i] = Vector.RandomVector().SetMagnitude(MaxForce)

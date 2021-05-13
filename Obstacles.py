import pygame
from vector import *
class Obstacle:
    def __init__(self, x, y, w, h):
        self.position = Vector(x, y)
        self.width = w
        self.height = h
        self.color = (0, 0, 0)
    def Draw(self, screen, color=None):
        if color == None:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.position.x, self.position.y, self.width, self.height) )
        else:
            pygame.draw.rect(screen, color, pygame.Rect(self.position.x, self.position.y, self.width, self.height) )

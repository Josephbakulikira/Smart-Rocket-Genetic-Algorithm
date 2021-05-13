from math import sqrt, pow, atan2, cos, sin, degrees, pi
from random import uniform

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(a, b):
        if type(b) != Vector:
            return Vector(a.x + b, a.y + b)
        return Vector(a.x + b.x, a.y + b.y)

    def __sub__(a, b):
        if type(b) != Vector:
            return Vector(a.x - b, a.y - b)
        return Vector(a.x - b.x, a.y - b.y)

    def __mul__(a, b):
        if type(b) != Vector:
            return Vector(a.x * b, a.y * b)
        return Vector(a.x * b.x, a.y * b.y)

    def GetMagnitude(self):
        return sqrt(pow(self.x,2) + pow(self.y,2))

    def Normalize(self):
        mag = self.GetMagnitude()
        return Vector(self.x/mag, self.y/mag)

    def Heading(self):
        angle = atan2(self.y, self.x)
        #degrees = 180 * angle / pi
        #return angle in radians
        return angle

    def RandomVector():
        v = Vector(uniform(-1, 1), uniform(-1, 1)).Normalize()
        return v

    def SetMagnitude(self, mag):
        self.Normalize()
        return Vector(self.x * mag, self.y * mag)

    def fromAngle(angle):
        return Vector(cos(angle), sin(angle))

    def units():
        return Vector(1, 1)

    def GetDistance(v1, v2):
        return sqrt( pow(v2.x - v1.x, 2) + pow(v2.y - v1.y, 2) )
    def __repr__(self):
        #debug
        return f'vector--> x:{self.x}, y:{self.y}'

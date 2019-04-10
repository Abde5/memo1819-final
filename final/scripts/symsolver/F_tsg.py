from sage.all import *

class UnitDisk:
    def __init__(self, name):
        self.name = name
        self.x = df.symbols('x_'+name, real=True)
        self.y = df.symbols('y_'+name, real=True)

    def adjacent(self,other):
        return []

    def no_adjacent(self, other):
        return ()

    def domain(self, eps):
        return [self.y >= 0, self.y <= eps]

x, y, xa, ya = var('x,y,xa,ya')
sol = solve([1 - (ya-y)**2 >= 1])

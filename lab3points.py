import math
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self, x, y):
        return self.x, self.y
    def move(self, x, y):
        self.x += x
        self.y += y
        return self.x, self.y
    def dist(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)


x = int(input())
y = int(input())
a = Point(x, y)
print(a.show(x, y))
print(a.move(x, y))
print(a.dist(x, y))
    
    
    
    
class shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class square(shape):
    def __init__(self):
        shape.__init__(self)
        self.length = int(input())
        
    def area(self):
        return self.length*self.length

a = square()
print (a.area())
class Dot:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        
    def moveDot(self, dx, dy):
        self.x += dx
        self.y += dy

    def getCoordinates(self):        
        return (self.x, self.y)

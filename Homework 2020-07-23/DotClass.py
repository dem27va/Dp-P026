class Dot:

    def __init__(self, name, x, y, color, size, marker):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.marker = marker
        
    def moveDot(self, dx, dy):
        self.x += dx
        self.y += dy

    def changeColor(self, color):
        self.color = color

    def changeMarker(self, marker):
        self.marker = marker

    def changeSize(self, size):
        self.size = size

    def drawDot(self):
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()     
        plt.scatter(self.x, self.y, color = str(self.color), s = self.size, marker = str(self.marker))
        ax.set_facecolor('gray')
        fig.set_figwidth(5)
        fig.set_figheight(5)
        plt.grid()
        plt.show()

    def getCoordinates(self):        
        return (self.x, self.y)

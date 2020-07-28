pi = 3.14

class Shape:

    def __init__(self, x, y, color='black', filled=False):
        self.x = x
        self.y = y
        self.color = color
        self.filled = filled

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled


class Rectangle(Shape):

    def __init__(self, length, width):
        #super().__init__()
        Shape.__init__(self)
        self.length = length
        self.width = width

    def get_length(self):
        return self.length

    def set_length(self, length):
        self.length = length

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_coordinates():
        return (self.x, self.y)

    def relocate(self, newX, newY):
        self.x = newX
        self.y = newY


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * pi * self.radius
    

class RightTriangle(Shape, Rectangle):
    def __init__(self, leg1, leg2):
        super().__init__()
        self.leg1 = leg1
        self.leg2 = leg2


rect1 = Rectangle(3,2)
c1 = Circle(4)

'''
print("Площадь прямоугольника rect1:", rect1.get_area())
print("Периметр прямоугольника rect1:", r1.get_perimeter())
print("Цвет прямоугольника rect1:", r1.get_color())
print("Залит ли прямоугольник rect1? ", r1.get_filled())
r1.set_filled(True)
print("алит ли прямоугольник rect1? ", r1.get_filled())
r1.set_color("orange")
print("Цвет прямоугольника rect1:", r1.get_color())



print("\nПлощадь круга c1:", format(c1.get_area(), "0.2f"))
print("Периметр круга c1:", format(c1.get_perimeter(), "0.2f"))
print("Цвет круга c1:", c1.get_color())
print("Залит ли круг с1? ", c1.get_filled())
c1.set_filled(True)
print("Залит ли круг с1? ", c1.get_filled())
c1.set_color("blue")
print("Цвет круга c1:", c1.get_color())
'''
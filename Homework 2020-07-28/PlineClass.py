from DotClass import Dot

class Pline:

    def __init__(self, name, dotsSet):
        self.name = name
        self.dotsSet = dotsSet
    

    def printPlineDots(self):
        for el in self.dotsSet:
            print('Линия {}. Координаты точки {}: {}, {}'.format(self.name, el.name, el.x, el.y))
        print('\n')            


    def addPoint (self, dotName, x, y):
        dot = Dot(dotName, x, y)
        self.dotsSet.add(dot)
    

    def hasPoint(self, x, y):
        for el in self.dotsSet:
            if el == (x, y):
                return True
            else:
                return False


    def relocatePoint(self, x, y, newX, newY):
        for el in self.dotsSet:
            if el.x == x and el.y == y:                
                dot = Dot(el.name, newX, newY)
                self.dotsSet.discard(el)
                self.dotsSet.add(dot)


    def clone(self, offsetX, offsetY):
        cloneSet = set()
        
        for el in self.dotsSet:
            dot = Dot(el.name + '_clone', el.x + offsetX, el.y + offsetY)
            cloneSet.add(dot)
        
        return Pline(self.name + '_clone', cloneSet)


    def deletePoint(self, x, y):
        for el in self.dotsSet:
            if el.x == x and el.y == y:
                self.dotsSet.discard(el)
                break       
        
    


    


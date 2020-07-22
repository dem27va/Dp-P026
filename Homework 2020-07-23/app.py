from DotClass import Dot

dot1 = Dot('A', 3, 3, 'blue', 100, '.')
dot2 = Dot('B', 1, 5, 'blue', None, 'H')
dot3 = Dot('C', -5, -3, 'green', None, 'o')
dot4 = Dot('D', 1, 1, 'yellow', None, '.')

print('Начальные координаты:\t', dot1.getCoordinates())
dot1.drawDot()

dot1.moveDot(-3, 9)
print('Измененные координаты:\t', dot1.getCoordinates())

dot1.changeColor('red')
dot1.drawDot()

dot1.changeMarker('x')
dot1.drawDot()

def drawAllDots(*dots):
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots()

    for d in dots:
        plt.scatter(d.x, d.y, color = str(d.color), s = d.size, marker = d.marker)        
    
    ax.set_facecolor('gray')
    fig.set_figwidth(7)
    fig.set_figheight(7)
    plt.grid()
    plt.show()

drawAllDots(dot1, dot2, dot3, dot4)

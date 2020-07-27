from DotClass import Dot
from PlineClass import Pline

def drawPline(*plines):
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots()

    for pline in plines:
        for dot in pline.dotsSet:
            plt.scatter(dot.x, dot.y, color = 'red', s = 50)        
        
    ax.set_facecolor('gray')
    fig.set_figwidth(5)
    fig.set_figheight(5)
    plt.grid()
    plt.xlim(-6, 6)
    plt.ylim(-6, 6)
    plt.show()


dotSet1 = set()
dotSet1.add(Dot('A', 1, 1))
dotSet1.add(Dot('B', 2, 1))
dotSet1.add(Dot('C', -1, -1))


pline1 = Pline('pl1', dotSet1)

print(pline1)
pline1.printPlineDots()
drawPline(pline1)

pline1.relocatePoint(1, 1, 1, 3)
pline1.printPlineDots()
drawPline(pline1)

pline2 = pline1.clone(-2, 0)
pline2.printPlineDots()
drawPline(pline1, pline2)

pline2.relocatePoint(-3, -1, -3, 2)
pline1.printPlineDots()
pline2.printPlineDots()
drawPline(pline1, pline2)

pline2.deletePoint(-3, 2)
pline1.printPlineDots()
pline2.printPlineDots()
drawPline(pline1, pline2)


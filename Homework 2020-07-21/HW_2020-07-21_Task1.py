numberOfRect = int(input('Введите количество прямоугольников: '))

def inputRectLocations(n):                          #Вводим координаты прямоугольников, определяемые двумя угловыми точками
    locationsArr = []
    for rectangle in range(n):                      #Перебираем прямоугольники
        twoPointsCoords = {}
        print('Введите координаты двух углов прямоугольника ' + str(rectangle + 1))
        twoPointsCoords['x1'] = int(input('x1: '))
        twoPointsCoords['y1'] = int(input('y1: '))
        twoPointsCoords['x2'] = int(input('x2: '))
        twoPointsCoords['y2'] = int(input('y2: '))
        locationsArr.append(twoPointsCoords)

    return locationsArr

rectLocationsArr = inputRectLocations(numberOfRect)

print(rectLocationsArr)


def calculateRectCoordinates(inputArr):
    rectanglesArr = []
    
    for rectangle in inputArr:
        rectCoordinatesSet = set()
        
        for x in range(min(rectangle['x1'], rectangle['x2']), max(rectangle['x1'], rectangle['x2']) + 1):       # +1 потому, что range() не захватывает последне значение и мы теряем координаты
            for y in range(min(rectangle['y1'], rectangle['y2']), max(rectangle['y1'], rectangle['y2']) + 1):
                pareOfCoordinates = (x, y)                  #записываем в кортеж пару координат каждой точки прямоугольника
                rectCoordinatesSet.add(pareOfCoordinates)   #добавляем в монжество координаты каждой точки прямоугольника
        
        rectanglesArr.append(rectCoordinatesSet)
    
    return rectanglesArr                                    #Возвращаем список множеств, содержащих кортежи, в которых записаны пары координат каждой точки прямоугольника

res = calculateRectCoordinates(rectLocationsArr)

#print(res)
#print(res[0])
for el in res:
    print(el)

def drawRect(coordSetArr):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    fig = plt.figure() 
    ax = fig.add_subplot(111) 

    for rectangle in coordSetArr:           #Перебираем прямоуголники в массиве с координатами
        xs = []                             #Создаем временный массив со всеми координатами X для текущего прямоугольника
        ys= []                              #Создаем временный массив со всеми координатами Y для текущего прямоугольника
        
        for coordPare in rectangle:         #Перебираем пары координат каждой точки текущего прямоугольника
            xs.append(coordPare[0])         #Заполняем массив координат X текущего прямоугольника
            ys.append(coordPare[1])         #Заполняем массив координат Y текущего прямоугольника

        rect = patches.Rectangle((min(xs), min(ys)), max(xs) - min(xs), max(ys) - min(ys), linewidth=1,edgecolor='r',facecolor='black', alpha = 0.5)
        ax.add_patch(rect)

    plt.xlim([-50, 50])
    plt.ylim([-50, +50])
    plt.show()

drawRect(res)

'''
rectCoord1 = set()
for x in range(min(x1, x2), max(x1,x2) + 1):
    for y in range(min(y1, y2), max(y1,y2) + 1):
        pareOfCoordinates = (x, y)
        rectCoord1.add(pareOfCoordinates)





def drawGraph(coordSet):
    import matplotlib.pyplot as plt
    xs = []
    ys = []
    for pare in coordSet:
        xs.append(pare[0])
        ys.append(pare[1])
    plt.scatter(xs, ys, s = 10)
    plt.show()

def drawRect(coordSet):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    xs = []
    ys = []
    for pare in coordSet:
        xs.append(pare[0])
        ys.append(pare[1])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rect1 = patches.Rectangle((min(xs), min(ys)), max(xs) - min(xs), max(ys) - min(ys), linewidth=1,edgecolor='r',facecolor='black', alpha = 0.5)
    ax.add_patch(rect1)

    plt.xlim([min(xs) - 1, max(xs) + 1])
    plt.ylim([min(ys) - 1, max(ys) + 1])

    plt.show()


#drawGraph(rectCoord1)
drawRect(rectCoord1)
'''



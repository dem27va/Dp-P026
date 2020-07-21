numberOfRectangles = int(input('Введите количество прямоугольников: '))

def inputRectLocations(numberOrRectangles):                          #Вводим координаты прямоугольников, определяемые двумя угловыми точками
    rectLocationsList = []
    for rectangle in range(numberOrRectangles):                      #Перебираем прямоугольники
        twoPointsCoords = {}
        print('Введите координаты двух углов прямоугольника ' + str(rectangle + 1))
        twoPointsCoords['x1'] = int(input('x1: '))
        twoPointsCoords['y1'] = int(input('y1: '))
        twoPointsCoords['x2'] = int(input('x2: '))
        twoPointsCoords['y2'] = int(input('y2: '))
        rectLocationsList.append(twoPointsCoords)

    return rectLocationsList                             #Возвращаем массив введенных координат прямоугольников


def calculateRectSurfaceCoords(rectLocationsList):             #Формируем множества всех точек прямоугольников по списку координат двух угловых точек каждого прямоугольника
    rectanglesArr = []
    
    for rectangle in rectLocationsList:
        rectCoordinatesSet = set()
        
        for x in range(min(rectangle['x1'], rectangle['x2']), max(rectangle['x1'], rectangle['x2']) + 1):       # +1 потому, что range() не захватывает последне значение и мы теряем координаты
            for y in range(min(rectangle['y1'], rectangle['y2']), max(rectangle['y1'], rectangle['y2']) + 1):
                rectCoordinatesSet.add((x, y))   #добавляем в монжество координаты всех точек прямоугольника
        
        rectanglesArr.append(rectCoordinatesSet)
    
    return rectanglesArr                                    #Возвращаем список множеств, содержащих кортежи, в которых записаны пары координат всех точек прямоугольника


def calculateRectIntersectArea(rectCoordSetsList):
    intersections = []
    intersectionsArea = 0

    for i in range(len(rectCoordSetsList)):             #Получаем координаты точек пересечений, поочередно проверяя пересечения множеств
        for j in range(i + 1, len(rectCoordSetsList)):
            if rectCoordSetsList[i] & rectCoordSetsList[j]:
                intersections.append(rectCoordSetsList[i] & rectCoordSetsList[j])

    for intersection in intersections:                  #Перебираем пересечения в массиве пересечений
        xs = []                                         #Создаем временный массив со всеми координатами X для текущего пересечения
        ys= []                                          #Создаем временный массив со всеми координатами Y для текущего пересечения        
        for coordPare in intersection:                  #Перебираем пары координат каждой точки текущего пересечения
            xs.append(coordPare[0])                     #Заполняем массив координат X текущего пересечения
            ys.append(coordPare[1])                     #Заполняем массив координат Y текущего пересечения
        
        intersectionsArea += (max(xs) - min(xs)) * (max(ys) - min(ys))

    return intersectionsArea

def calculateGrossrectangle(rectCoordSetsList):
    grossXs = []
    grossYs= []
    
    for rectangle in rectCoordSetsList: 

        for coordPare in rectangle: 
            grossXs.append(coordPare[0]) 
            grossYs.append(coordPare[1])

    grossrectangleCoordinatesSet = set()
    
    for x in range(min(grossXs), max(grossXs) + 1):                           # +1 потому, что range() не захватывает последне значение и мы теряем координаты
        for y in range(min(grossYs), max(grossYs) + 1):
            grossrectangleCoordinatesSet.add((x, y))     #добавляем в монжество координаты всех точек прямоугольника
    
    return grossrectangleCoordinatesSet


def drawRect(rectCoordSetsList, grossrectangle):
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    fig = plt.figure() 
    ax = fig.add_subplot(111) 

    for rectangle in rectCoordSetsList:                 #Перебираем прямоуголники в массиве с координатами
        xs = []                                         #Создаем временный массив со всеми координатами X для текущего прямоугольника
        ys= []                                          #Создаем временный массив со всеми координатами Y для текущего прямоугольника        
        for coordPare in rectangle:                     #Перебираем пары координат каждой точки текущего прямоугольника
            xs.append(coordPare[0])                     #Заполняем массив координат X текущего прямоугольника
            ys.append(coordPare[1])                     #Заполняем массив координат Y текущего прямоугольника

        rect = patches.Rectangle((min(xs), min(ys)), max(xs) - min(xs), max(ys) - min(ys), linewidth = 1, edgecolor = 'black', facecolor = 'green', alpha = 0.5)
        ax.add_patch(rect)
    
    grossXs = []
    grossYs = []
    for grossCoord in grossrectangle:
        grossXs.append(grossCoord[0])
        grossYs.append(grossCoord[1])
    
    rectGross = patches.Rectangle((min(grossXs), min(grossYs)), max(grossXs) - min(grossXs), max(grossYs) - min(grossYs), linestyle = 'dotted', linewidth = 2, edgecolor = 'red', facecolor = 'none')
    ax.add_patch(rectGross)

    plt.xlim([-50, 50])
    plt.ylim([-50, +50])
    plt.grid(which='both')
    plt.show()


rectLocationsList = inputRectLocations(numberOfRectangles)

rectSurfaceCoords = calculateRectSurfaceCoords(rectLocationsList)

print(rectSurfaceCoords)

intersectionsArea = calculateRectIntersectArea(rectSurfaceCoords)
print('Общая площадь пересечения всех прямоугольников: ', intersectionsArea)
grossrectangle = calculateGrossrectangle(rectSurfaceCoords)
print('Координаты глобального прямоугольника: ', grossrectangle)

drawRect(rectSurfaceCoords, grossrectangle)

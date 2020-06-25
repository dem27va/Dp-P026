inStr = input('Введите строку, содержащую скобки: ')

openBrackets = ['(', '[', '{']
go = True

#Считаем пары скобок
roundOpen = 0
roundClosed = 0
squareOpen = 0
squareClosed = 0
curlyOpen = 0
curlyClosed = 0

for el in inStr:
    if el == '(':
        roundOpen +=1
    if el == '[':
        squareOpen +=1
    if el == '{':
        curlyOpen +=1
    if el == ')':
        roundClosed +=1
    if el == ']':
        squareClosed +=1
    if el == '}':
        curlyClosed +=1

#Если кол-во открывающихся скобок не соответствует кол-ву закрывающихся - у нас ошибка
if (roundOpen != roundClosed) or (squareOpen != squareClosed) or (curlyOpen != curlyClosed):
    print('Ошибка! Количество открывающихся скобок не соответствует количеству закрывающихся')
    print('():', roundOpen + roundClosed, '[]:', squareOpen + squareClosed, '{}:', curlyOpen + curlyClosed)

#В противном случае проверяем последовательность расстановки скобок
else:
    #Подсчитываем общее количество скобок
    bracketsCount = roundOpen + roundClosed + squareOpen + squareClosed + curlyOpen + curlyClosed    
    
    while go:

        nextIter = False
        
        #Идем по строке и ищем закрывающуюся скобку
        for i in range(len(inStr)):
            if inStr[i] == ')' or inStr[i] == ']' or inStr[i] == '}':       
        
                #Определяем какую соответствующую открывающуюся скобку мы будем искать
                if inStr[i] == ')':
                    target = '('
                elif inStr[i] == ']':
                    target = '['
                elif inStr[i] == '}':
                    target = '{'
        
                #Создаем временную копию списка откорывающихся скобок и удааляем из него скобку, которую мы ищем 
                # таким образом мы получаем список "неправильных" открывающихся скобок
                wrongOpenBrackets = openBrackets.copy()
                wrongOpenBrackets.remove(target)

                #выделяем подстроку от начала строки до закрывающейся скобки
                subStr = inStr[:i]

                #Идем по подстроке в обратном направлении и ищем соответствующую открывающуюся скобку
                for j in range(i-1, -1, -1):
                    #Если символ подстроки является нужной нам открывающейся скобкой - 
                    # удаляем пару скобок при помощи slice и конкатенации, уменьшаем счетчик скобок,
                    # присваиваем значение "истина" флагу перехода к следующей итерации цикла поиска закрывающейся скобки
                    # и выходим из цикла перебора подстроки
                    if subStr[j] == target:
                        inStr = subStr[0 : j] + inStr[(j+1) : i] + inStr[(i+1) : ]
                        bracketsCount -= 2                        
                        nextIter = True
                        break
                    #Если нам встречается "неправильная" открывающаяся скобка - 
                    # значит в последовательности скобок ошибка, 
                    # присваиваем значение "ложь" флагу GO, чтобы выйти из самого верхнего цикла
                    elif subStr[j] in wrongOpenBrackets:
                        print('Ошибка! Неправильная последовательность скобок')
                        go = False
                        nextIter = True
                        break
                    #В любом другом случае просто продолжаем перебор подстроки
                    else:
                        continue                
                
            if nextIter:
                break
        
        if bracketsCount == 0:
            print('Скобки в порядке!')
            go = False

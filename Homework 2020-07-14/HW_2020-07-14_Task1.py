#Проверка ввода
def inputCorrectString():
    stringLenExceeded = True
    while stringLenExceeded:
        string = input('Введите строку\n(до 498 символов):\t')
        if len(string) > 498:
            print('Неправильный ввод. Длина введенной стороки - {} символов.'.format(len(string)))
        else:
            stringLenExceeded = False
        
    return string


def printDigitsFirst(string, currentCharacter = 0, charactersPrintedCount = 0, allDigitsPrinted = False):

    if charactersPrintedCount == len(string):
        return

    else:
        #ЦИФРА и НЕ все цифры напечатаны
        if string[currentCharacter].isnumeric() and allDigitsPrinted == False:
            #Если не последний символ
            if (currentCharacter + 1) < len(string):
                #выводим текущий символа, счетчик напечатаных символов + 1, возвращаем функцию для следующего сивола
                print(string[currentCharacter], end = '')
                charactersPrintedCount += 1                
                return printDigitsFirst(string, currentCharacter + 1, charactersPrintedCount, allDigitsPrinted)
            #Если последний символ
            else:
                #отмечаем что все цифры напечатаны, выводим текущий символ, счетчик напечатаных символов + 1,
                # возвращаем функцию с обнуленным текущим символом
                allDigitsPrinted = True
                print(string[currentCharacter], end = '')
                charactersPrintedCount += 1                
                return printDigitsFirst(string, 0, charactersPrintedCount, allDigitsPrinted)                            
        

        #ЦИФРА и все цифры напечатаны
        elif string[currentCharacter].isnumeric() and allDigitsPrinted == True:
            #Если не последний символ
            if (currentCharacter + 1) < len(string):
                #возвращаем вызов функцию для следующего сивола
                return printDigitsFirst(string, currentCharacter + 1, charactersPrintedCount, allDigitsPrinted)                
            #Если последний символ
            else :
                #возвращаем вызов функции с обнуленным текущим символом
                return printDigitsFirst(string, 0, charactersPrintedCount, allDigitsPrinted)
                


        #СИМВОЛ и НЕ все цифры напечатаны
        elif not string[currentCharacter].isnumeric() and allDigitsPrinted == False:
            #Если не последний символ
            if (currentCharacter + 1) < len(string):
                #возвращаем вызов функцию для следующего сивола
                return printDigitsFirst(string, currentCharacter + 1, charactersPrintedCount, allDigitsPrinted)
            #Если последний символ
            else:
                #Отмечаем что все цифры напечатаны, возвращаем вызов функцию с обнуленным текущим символом
                allDigitsPrinted = True                
                return printDigitsFirst(string, 0, charactersPrintedCount, allDigitsPrinted)
                


        #СИМВОЛ и все цифры напечатаны
        elif not string[currentCharacter].isnumeric() and allDigitsPrinted == True:
            #Если не последний символ
            if (currentCharacter + 1) < len(string):
                #выводим текущий символ, счетчик напечатаных символов + 1, возвращаем функцию для следующего сивола
                print(string[currentCharacter], end = '')
                charactersPrintedCount += 1               
                return  printDigitsFirst(string, currentCharacter + 1, charactersPrintedCount, allDigitsPrinted)                
            #Если последний символ
            else:
                #выводим текущий символ, счетчик напечатаных символов + 1, возвращаем функцию с обнуленным текущим символом                
                print(string[currentCharacter], end = '')
                charactersPrintedCount += 1                
                return printDigitsFirst(string, 0, charactersPrintedCount, allDigitsPrinted)

inputString = inputCorrectString()

print('Результат:\t\t', end = '')
printDigitsFirst(inputString)
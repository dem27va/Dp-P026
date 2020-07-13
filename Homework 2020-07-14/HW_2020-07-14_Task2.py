#Ввод строки с учетом символов, которые должны игнорироваться пр проверке на палиндром
def getRefinedString():
    #записываем в строку символы, которые должны игнорироваться
    charactersToIgnore = input('Введите символы, которые будут игнорироваться при проверке: ')
    #Вводим строку и переводим все символы в нижний регистр
    inputString = input('Введите строку: ').lower()

    #Удаляем игнорируемые символы из строки
    for ch in charactersToIgnore:        
        inputString = inputString.replace(ch, '')

    return inputString


def is_palindrome(string, i = 0):
    if len(string) == 0:                    #Если строка пустая - выводим соответствующее сообщение
        print('Введена пустая строка')
        return
    
    elif i > len(string) // 2:              #Если мы дошли до итератора, который больше, чем половина длины строки - значит введен палиндром
        print('Палиндром')
        return    
    
    else:
        if string[i] == string[-i-1]:       #Если зеркально расположенные символы равны - рекурсивно вызываем ф-цию для следующего итератора
            return is_palindrome(string, i + 1)
        elif string[i] != string[-i-1]:     #Если зеркально расположенные символы не равны - не палиндром
            print('Не палиндром')
            return 

refinedInputString = getRefinedString()
is_palindrome(refinedInputString)

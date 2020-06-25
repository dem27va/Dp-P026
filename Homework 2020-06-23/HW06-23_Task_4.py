#Пользователь вводит целое число.
#Определить является ли чесло однозначным, двузначным, трехзначным или содержит больше символов

inputNumber = input('Введите целое число: ')

#Проверяем положительно или отрицательное введено число
if inputNumber[0] == '-':
    digitsCount = len(inputNumber) - 1
    sign = 'отрицательное'
else:
    digitsCount = len(inputNumber)
    sign = 'положительное'

#Записываем в строчную переменную сколькозначное число введено
if digitsCount == 1:
    result = 'однозначное'
elif digitsCount == 2:
    result = 'двузначное'
elif digitsCount == 3:
    result = 'трезначное'
elif digitsCount > 3:
    result = 'содержащее больше четырех знаков'
else:
    result = 'какое-то другое'

#Если введен нуль - пишем, что введен нуль, в противном случае пишем какое число введено
if inputNumber == '0':
    print('Введен нуль')
else:
    print('Введено {} {} число '.format(sign, result))


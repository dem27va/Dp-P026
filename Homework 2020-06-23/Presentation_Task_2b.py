#Задано чотирицифрове натуральне число. Записати число в реверсному порядку.

inputNumber = int(input('Введите четырехзначное число: '))

outDigit1 = (inputNumber // 1) % 10
outDigit2 = (inputNumber // 10) % 10
outDigit3 = (inputNumber // 100) % 10
outDigit4 = (inputNumber // 1000) % 10

outputNumber = str(outDigit1) + str(outDigit2) + str(outDigit3) + str(outDigit4)

print(outputNumber)

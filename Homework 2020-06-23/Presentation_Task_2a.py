#Задано чотирицифрове натуральне число. Знайти добуток цифр цього числа.

inputNumber = int(input('Введите четырехзначное число: '))

outDigit1 = (inputNumber // 1) % 10
outDigit2 = (inputNumber // 10) % 10
outDigit3 = (inputNumber // 100) % 10
outDigit4 = (inputNumber // 1000) % 10

outputNumber = outDigit1 * outDigit2 * outDigit3 * outDigit4

print(outputNumber)
#Пользователь вводит число. Посчитать сууму цифр в числе

inputNumber = input('Введите число: ')

count = len(inputNumber)

result = 0

for i in range(count):
    result += (int(inputNumber) //10**i) % 10

print(result)

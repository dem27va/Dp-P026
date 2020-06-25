#Пользователь вводит значения 5 чисел. Определить мин и макс числа

count = 5
inputArr = []

for i in range(count):
    inputArr.append(float(input('Введите число {}: '.format(i + 1))))

mini = inputArr[0]
maxi = inputArr[0]

for el in inputArr:   
    if el < mini:
        mini = el
    
    if el >maxi:
        maxi = el

print('Наименьшее число - "{}", наибольшее число - "{}"'.format(mini, maxi))
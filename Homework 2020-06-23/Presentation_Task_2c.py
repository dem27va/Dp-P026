#Задано чотирицифрове натуральне число. Посортувати цифри, що входять в дане число.

#Получаем строку с числом и превращаем ее в список
inputNumberArr = list(input('Введите четырехзначное число: '))    #Работает не только для четырехзначных чисел

n = len(inputNumberArr)

#Выполняем сортировку. Проходим по массиву и меняем местами соседние элементы,
# если предыдущий элемент больше следующего.
#Но можно реализовать сортировку просто методом .sort()

for i in range(n):
    for j in range(n-1):
        if inputNumberArr[j]> inputNumberArr[j+1]:
            inputNumberArr[j], inputNumberArr[j+1] = inputNumberArr[j+1], inputNumberArr[j]

outputNumber = ''.join(inputNumberArr)    #Соединяем отсортированный список в строку

print(outputNumber)
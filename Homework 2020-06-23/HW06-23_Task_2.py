#Пользователь вводит число в десятичной системе. Посчитать сколько 0 и 1 в этом числе в двоичной системе

inputDecimal = int(input('Введите число: '))

binaryNumber = ''
zerosCount = 0
onesCount = 0

while inputDecimal > 0:
    binaryNumber += str(inputDecimal % 2)
    inputDecimal = inputDecimal // 2

#Цикл выше возвращает число в двоичной системе в обратной последовтельности.
# Для этой конкретной задачи такая особенность не играет роли,
# но для красоты двоичное число можно развернуть
binaryNumber = ''.join(reversed(binaryNumber))

for el in binaryNumber:
    if el == '0':
        zerosCount += 1
    else:
        onesCount += 1    

print('Введенное число в двоичной системе:', binaryNumber)
print('Введенное число в двоичной системе содержит {} нулей и {} единиц'.format(zerosCount, onesCount))

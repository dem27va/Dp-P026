start = int(input('Введите десятичный код начала диапазона символов: '))
finish = int(input('Введите десятичный код конца диапазона символов: '))

for i in range(start, finish + 1):
    print('Десятичный код:', i, '\t символ - "{}"'.format(chr(i)))


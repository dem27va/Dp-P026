st1 = input('Введите строку 1: ')
st2 = input('Введите строку 2: ')

if len(st1) > len(st2):
    print ('Строка 1 больше стороки 2')
elif len(st1) < len(st2):
    print ('Строка 2 больше стороки 1')
else:
    for i in range(len(st1)):
        if st1[i] > st2[i]:
            print ('Строка 1 больше стороки 2')
            break
        if st1[i] < st2[i]:
            print ('Строка 2 больше стороки 1')
            break
        if st1[i] == st2[i]:
            continue
        
    if i == (len(st1) -1):
        print('Строки одинаковые')
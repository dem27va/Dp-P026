from class_Animal import *

animalList = []

animalList.append(Animal('Зверёк'))
animalList.append(Dog('Бобик'))
animalList.append(Shepherd('Зверюга'))
animalList.append(Cat('Шерстяной'))
animalList.append(Fish('Пузырек'))

for i in range(len(animalList)):
    print(animalList[i].pet())
    print(animalList[i].eat())
    print(animalList[i].scold())
    print(animalList[i].play())
    print(animalList[i].serve(), '\n')


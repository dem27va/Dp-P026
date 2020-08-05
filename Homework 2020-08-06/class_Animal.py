class Animal:

    def __init__(self, nickname):
        self.nickname = nickname
    
    def pet(self):
        action = '{} {}'.format(self.nickname, 'доволен')
        return action
    
    def eat(self):
        action = '{} {}'.format(self.nickname, 'кушает')
        return action

    def scold(self):
        action = '{} {}'.format(self.nickname, 'пугается')
        return action

    def play(self):
        action = '{} {}'.format(self.nickname, 'играет')
        return action

    def serve(self):
        action = '{} {}'.format(self.nickname, 'что-то делает')
        return action


class Dog(Animal):
    def __init__(self, nickname):
        super().__init__(nickname)        

    def pet(self):
        action = '{} {}'.format(self.nickname, 'виляет хвостом')
        return action

    def eat(self):
        action = '{} {}'.format(self.nickname, 'грызет кость')
        return action

    def scold(self):
        action = '{} {}'.format(self.nickname, 'поджимает уши, немного скулит')
        return action

    def play(self):
        action = '{} {}'.format(self.nickname, 'играет с тенисным мячиком')
        return action

    def serve(self):
        action = '{} {}'.format(self.nickname, 'приносит палку')
        return action


class Cat(Animal):
    def __init__(self, nickname):
        super().__init__(nickname)        

    def pet(self):
        action = '{} {}'.format(self.nickname, 'мурчит')
        return action

    def eat(self):
        action = '{} {}'.format(self.nickname, 'лакает молоко')
        return action

    def scold(self):
        action = '{} {}'.format(self.nickname, 'игнорирует хозяина, кушает и спит, чуть позже гадит хозяину в тапок ')
        return action

    def play(self):
        action = '{} {}'.format(self.nickname, 'играет с клубком ниток')
        return action

    def serve(self):
        action = '{} {}'.format(self.nickname, 'охотится на мышь')
        return action


class Fish(Animal):
    def __init__(self, nickname):
        super().__init__(nickname)        

    def pet(self):
        action = '{} {}'.format(self.nickname, 'молчит, пускает пузыри')
        return action

    def eat(self):
        action = '{} {}'.format(self.nickname, 'ест рыбий корм')
        return action

    def scold(self):
        action = '{} {}'.format(self.nickname, 'прячется в свой подводный домик')
        return action

    def play(self):
        action = '{} {}'.format(self.nickname, 'молчит, пускает пузыри')
        return action

    def serve(self):
        action = '{} {}'.format(self.nickname, 'молчит, пускает пузыри')
        return action


class Shepherd(Dog):
    def __init__(self, nickname):
        super().__init__(nickname)        

    def pet(self):
        action = '{} {}'.format(self.nickname, 'виляет хвостом')
        return action

    def eat(self):
        action = '{} {}'.format(self.nickname, 'грызет кость')
        return action

    def scold(self):
        action = '{} {}'.format(self.nickname, 'поджимает уши, немного скулит')
        return action

    def play(self):
        action = '{} {}'.format(self.nickname, 'играет с тенисным мячиком')
        return action

    def serve(self):
        action = '{} {}'.format(self.nickname, 'стережет скот')
        return action


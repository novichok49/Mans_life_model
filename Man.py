from random import randint
from House import House


class Man:
    def __init__(self, name):
        self.name = name
        self.fullnes = 50
        self.house = None

    def __str__(self):
        return '{} голод:{}'.format(self.name, self.fullnes)

    def eat(self):
        if self.house.food >= 10:
            self.house.food -= 10
            self.fullnes += 10
            print('{0} покушал'.format(self.name))
        else:
            print('У {0} недостаточно еды нужно ещё {1}'.format(self.name, 10 - self.house.food))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 50
        self.fullnes -= 20

    def watch_tv(self):
        print('{} посмотрел телевизор'.format(self.name))
        self.fullnes -= 20

    def buy_food(self):
        if self.house.money < 30:
            print('{} денег нет!'.format(self.name))
        else:
            print('{} купил еды'.format(self.name))
            self.house.money -= 30
            self.house.food += 30

    def act(self):
        if self.fullnes < 0:
            print('{} умер'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullnes <= 20:
            self.eat()
            if self.house.food <= 10:
                self.buy_food()
        elif self.house.food <= 10:
            self.buy_food()
        elif self.house.money <= 30:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_tv()

    def enter_house(self, house):
        self.house = house
        self.fullnes -= 10
        print('{} заехал в дом'.format(self.name))

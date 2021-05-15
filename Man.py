from random import randint

FULLNES_SPENDS = {"work": 20,
                  "watch_tv": 10,
                  "enter_house": 10}
FULLNES_FILL = 20

FOOD_SPENDS = 20
FOOD_FILL = 20

MONEY_SPENDS = 20
MONEY_FILL = 20


class Man:
    def __init__(self, name, start_fullnes=50, house=None):
        self.name = name
        self.fullnes = start_fullnes
        self.house = house

    def __str__(self):
        return '{} голод:{}'.format(self.name, self.fullnes)

    def eat(self):
        if self.house.food - FOOD_SPENDS >= 0:
            self.house.food -= FOOD_SPENDS
            self.fullnes += FULLNES_FILL
            print('{} покушал'.format(self.name))
        else:
            print('Еды нет!!!')

    def work(self):
        self.house.money += MONEY_FILL
        self.fullnes -= FULLNES_SPENDS["work"]
        print('{} сходил на работу'.format(self.name))

    def watch_tv(self):
        print('{} смотрел телевизор весь день'.format(self.name))
        self.fullnes -= FULLNES_SPENDS["watch_tv"]

    def buy_food(self):
        if self.house.money - MONEY_SPENDS >= 0:
            self.house.money -= MONEY_SPENDS
            self.house.food += FOOD_FILL
            print('{} купил еды'.format(self.name))
        else:
            print('Денег нет!!!')

    def act(self):
        if self.fullnes < 0:
            print('{} умер от голода!'.format(self.name))
            return
        if self.fullnes < max(FULLNES_SPENDS.values()):
            if self.house.food < FOOD_SPENDS:
                print('{} видит, что мало еды в холодильнике и хочет сходить в магазин'.format(self.name))
                if self.house.money < MONEY_SPENDS:
                    print('{} видит, что мало денег и идёт работать'.format(self.name))
                    self.work()
                    self.buy_food()
                    self.eat()
                else:
                    self.buy_food()
                    self.eat()
            else:
                self.eat()
        else:
            dice = randint(1, 6)
            if dice == 1:
                self.work()
            else:
                self.watch_tv()

    def enter_house(self, house):
        self.house = house
        self.fullnes -= FULLNES_SPENDS["enter_house"]
        print('{} заехал в дом'.format(self.name))

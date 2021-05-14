class House:
    def __init__(self):
        self.food = 20
        self.money = 100

    def __str__(self):
        return 'Осталось {} еды в доме, денег {}'.format(self.food, self.money)

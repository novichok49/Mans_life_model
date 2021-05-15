class House:
    def __init__(self, start_food=20, start_money=0):
        self.food = start_food
        self.money = start_money

    def __str__(self):
        return 'Осталось {} еды в доме, денег {}'.format(self.food, self.money)

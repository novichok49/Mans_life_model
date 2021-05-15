from House import House
from Man import Man


citizens = [Man('Vasya'), Man('Misha')]
our_house = House()
for citizen in citizens:
    citizen.enter_house(our_house)
for day in range(1, 366):
    print('|||||||||| День {} ||||||||||||'.format(day))
    for citizen in citizens:
        citizen.act()
    for citizen in citizens:
        print(citizen)
    print(our_house)

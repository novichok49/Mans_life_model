from House import House
from Man import Man

vasya = Man('Vasya')
misha = Man('Misha')
our_house = House()
vasya.enter_house(house=our_house)
misha.enter_house(house=our_house)
for day in range(1, 21):
    print('|||||||||| День {} ||||||||||||'.format(day))
    vasya.act()
    misha.act()
    print(vasya)
    print(misha)
    print(our_house)

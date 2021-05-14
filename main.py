from Man import Man

vasya = Man('Vasya')
misha = Man('Misha')
for day in range(1, 366):
    print('|||||||||| День {} ||||||||||||'.format(day))
    vasya.act()
    misha.act()
    print(vasya)
    print(misha)

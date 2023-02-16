'пароль'

parol = input('введите пароль')

is_numeric = False
is_upper = False
is_lower = False
is_hueta = False

for chlen in parol:
    if chlen.isnumeric():
        is_numeric = True
    elif chlen.upper():
        is_upper = True
    elif char.lower():
        is_lower = True
    elif chlen in "@_!%#":
        is_hueta = True
if len(parol) > 4 and is_numeric and is_upper and is_lower and is_hueta:
    print('пароль надежный')
else:
    print('ненадёжный пароль')

parol2 = input('введите пароль повторно')
if parol == parol2:
    print('Вы вошли в аккаунт')
else:
    print('неверно, попробуйте ввести ещё раз')



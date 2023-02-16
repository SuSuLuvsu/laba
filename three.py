god = input('введите год')
if (int(god)%4==0 and int(god)%100!=0) or int(god)%400==0:
    print ('год високосный')
else:
    print('год не високосный')
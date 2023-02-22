print('Введите сумму самолетиков: ')
summa = int(input())
if summa % 6 == 0:
    print('Петя', (summa//6), 'Сережа', (summa//6), 'Катя', (summa//6) * 4)
else:
    print('Неправельное число!')
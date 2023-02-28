z=int(input("Введите число до 10 которое необходимое найти: "))
if z >= 100:
    print('Неверное число. Выполните условия запроса!!!')
else:
    import random
    massive=[]
    n=int(input("Введите длинну массива: "))
    for k in range(1,n+1):
        massive.append(random.randint(0,10))
    print(massive)
    sum = 0
    n = massive
    for i in massive:
        if i == z:
            sum += 1
    print(sum, '- нужных цифр в массиве!')
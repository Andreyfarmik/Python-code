x =int(input("Введите сумму натуральных число S: "))
y =int(input("Введите произведение натуральных число P: "))
if x and y >= 1000:
    print('Условия задачи нарушены!!! Введите числа до 1000: ')
else:
    mass = []
    for i in range(x + y):
        if i == (x * i - y)**0.5:
            mass.append(i)
    print(*mass if len(mass) == 2 else mass + mass)
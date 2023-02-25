n =int(input("Введите число - предел для определения границы возведения 2 в степень: "))
m = 1
while m < n:
    if(m < n):
        if (m * 2 > n):
            break
        else:
            m = m * 2
            print(m)
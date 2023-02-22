print('Введите шестизначное число билета: ')
num = int(input())
num1 = num // 1000
num2 = num % 1000
c = num1 % 10
i = num1 // 10
b = i % 10
a = i // 10
summ1 = a + b + c
c = num2 % 10
i = num2 // 10
b = i % 10
a = i // 10
summ2 = a + b + c
print(summ1, '||', summ2)
if summ1 == summ2:
    print('Да это счастливый билет!')
else:
    print('Нет, не повезло.')
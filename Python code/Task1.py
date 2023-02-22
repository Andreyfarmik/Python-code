print('Введите трехзначное число: ')
num = int(input())
c = num % 10
i = num // 10
b = i % 10
a = i // 10
summ = a + b + c
print(summ)
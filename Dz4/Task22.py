print('Введите первую группу чисел через пробел: ')
a = [int(x) for x in input().split()]
print('Введите вторую группу чисел через пробел: ')
b = [int(x) for x in input().split()]
list1 = set(a)
list2 = set(b)
mura = list1.intersection(list2)
mura1 = list(mura)
mura1.sort()
print(mura1)

print('Введите колличество ягод с разных кустов через пробел: ')
a = [int(x) for x in input().split()]
list1 = list(a)
list2 = list()
for i in range(len(list1) -1):
    list2.append(list1[i-1] + list1[i] + list1[i+1])
list2.append(list1[-2] + list1[-1] + list1[0])
print(max(list2))

import random
massive=[]
n=int(input("Введите колличество монет: "))
for k in range(1,n+1):
    massive.append(random.randint(0,1))
print(massive)
sum = 0
n = massive
for i in massive:
    if i == 0:
        sum += 1
print(sum, '- монет нужно перевернуть перфекционисту!')
import random
massive=[]
n=int(input("Размер массива: "))
m=int(input("Введите границу - число: "))
for k in range(1,n+1):
    massive.append(random.randint(1,m))
print(massive)
b=int(input("Введите число поиска: "))
nums=[abs(b-i) for i in massive]
print(massive[nums.index(min(nums))])

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('введите натуральное число '))
list = []
for i in range(2,n):
    k = False
    for j in range(2, i):
        if i % j == 0:
            k = True
            break
    if n % i == 0 and k == False:
        print(i,end=" ")
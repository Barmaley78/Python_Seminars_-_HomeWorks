# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

a = int(input('Введите натуральное число '))
for i in range(a):
    print((-3) ** i,end=" ")
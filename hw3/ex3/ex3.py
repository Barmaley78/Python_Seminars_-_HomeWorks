# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [4.45,6.12,8.78,2.11,4.65,3.05,5.01,7.44]
mind = 1.1
maxd = 0.0
for i in range(len(list)-1):
    a = list[i] % 1
    if a>maxd:
        maxd = a
    elif a<mind:
        mind = a
print(list)
print(maxd-mind)
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] 
# - список на основе n, а позиции элементов lst2=[3,1].

import random
random.seed()
n = int(input('введите число '))
lst1 = []
lst2 = []
for i in (0,1):
    lst2.append(random.randint(0, n))
for i in range(n):
    lst1.append(random.randint(-n, n))
print(lst1)
print(lst2)
print(lst1[lst2[0]] * lst1[lst2[1]])
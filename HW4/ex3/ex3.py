# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.

import random
random.seed()
lim = 10
list = []
for i in range(lim):
    list.append(random.randint(0, 10))
print(list)
udlist = []
for i in list:
    if list.count(i) == 1:
       udlist.append(i) 
print(udlist)

exit() 
# уникальные значения
ualist = []
ua = set(list)
for i in ua:
    ualist.append(i)
print(ualist)

a = [1,2,2,2,2,3,1,4]
print(set(a))

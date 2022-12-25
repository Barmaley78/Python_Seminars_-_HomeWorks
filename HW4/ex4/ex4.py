# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
random.seed()

k = int(input('введите степень многочлена '))
a1 = open('data.txt', 'w')
list = []
s1 = '=0'
for i in range(k+1):
    list.append(random.randint(0,101))
    if list[i] != 0:
        if i == 0:
            s1 ='+' + str(list[i]) + s1
        elif i == 1:
            s1 ='+' + str(list[i]) +'*x' + s1
        elif i == k:
            s1 =str(list[i]) +'*x^' + str(i) + s1
        else:
            s1 ='+' + str(list[i]) +'*x^' + str(i) + s1
a1.writelines(s1)
a1.close()
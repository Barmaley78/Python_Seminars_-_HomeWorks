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

exit()
import random
file = open('file.txt', 'w')

k = int(input('k = '))
res = ""

for i in range(k,-1, -1):
    f = ""
    a = random.randrange(0,100)
    if a > 0:
        f = str(a) + '*x^' + str(i) + ' + '
    res += f
if len(res) > 0:
    res += ' = 0'
else:
    print('No arguments')

res = res.replace(' 1*x', ' x').replace('x^1', 'x').replace('*x^0', '').replace('+  ', '').replace('+  +', '+')
file.write(res)
file.close()

# от Cергея

from random import randint

k = int(input('Insert equation power: '))
koefs = list()
for i in range(1, k + 2):
    koefs.append(randint(1, 100))

ans = list()
for i in range(len(koefs)):
    if k == 1:
        ans.append(f'{koefs[i]}*x')
    elif k == 0:
        ans.append(f'{koefs[i]}')
    else:
        ans.append(f'{koefs[i]}*x**{k}')
    flag = randint(0, 1)
    if flag == 1:
        ans.append('+')
    elif flag == 0:
        ans.append('-')
    k -= 1

ans.pop(-1)
ans.append('=0')
fout = open('output.txt', 'w')
fout.write(''.join(ans))
fout.close()

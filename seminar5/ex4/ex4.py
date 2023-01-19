# 4.Саша и Галя коллекционируют монетки. Каждый из них решил записать номиналы монеток из своей коллекции.
# Получилось два списка. Эти списки поступают на вход программы в виде двух строк из целых чисел, 
# записанных через пробел. Необходимо выделить значения, присутствующие в обоих списках и оставить среди
# них только четные. Результат вывести на экран в виде строки полученных чисел в порядке их возрастания 
# через пробел.

# При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), 
# подумайте что.

# d1 = '1 2 5 1 1 10 2'
# d2 = '5 2 2 1 1 1 5'

# def get_cur(s):
#     l = list(map(int, s.split()))
#     l1 = []
#     [l1.append(x) for x in l if x not in l1]
#     return l1

# l1 = get_cur(d1)
# print(l1)
# l2 = get_cur(d2)
# print(l2)


s = list(map(int, input().split()))
g = list(map(int, input().split()))
print(*sorted(filter((lambda i: not i%2), (i for i in s if g.count(i)))))

exit()

sasha = '1 5 15 20 10 50'
gala = '2 5 25 10 20'
f = lambda x: list(filter(lambda a: int(a)%2 == 0, x.split(" ")))
result = set(f(sasha)).intersection(set(f(gala)))

print(*sorted(list(result)))

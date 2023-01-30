# 5. Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся 
# на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.
# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.

lst = list(map(lambda z: z ** 2,filter(lambda x: not x % 9, range(10, 99))))
print(sum(lst))

exit()
l = [i for i in range(10, 100)]
l1 = list(filter(lambda x: x % 9 == 0, l))
l2 = sum(list(map(lambda x: x**2, l1)))
print(l2)
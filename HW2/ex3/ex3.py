# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def f(k):
    p = ((k+1)/k) ** k
    return p

n = int(input('введите натуральное число '))
list = []
sum = 0
for i in range(n):
    list.append(round(f(i+1),2))
    sum += list[i]
print(list)
print(sum)
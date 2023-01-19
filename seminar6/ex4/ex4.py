# 4 Вводится натуральное число N. С помощью list comprehension сформировать двумерный список 
# размером N x N, состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - 
# это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла). 
# Результат вывести в виде таблицы чисел как показано в примере ниже.

# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

n = int(input('введите размерность '))
# list = [[int(i==j) for j in range(n)] for i in range(n)]
k = 0
list = [[(int(i)+1)*(int(j)+1) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        print((list[i][j]), end=' ')
    print()
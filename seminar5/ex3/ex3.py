# 3 Вводится список в виде вещественных чисел в одну строку через пробел. Сначала нужно сформировать список 
#   из введенной строки. Затем, все отрицательные значения в этом списке заменить на -1.0. Результат вывести 
#   на экран в виде строки чисел через пробел. Программу следует реализовать с использованием 
#   функции enumerate.

a=list(map(float,input().split()))
for i ,r in enumerate(a):
    if r<0:
        a[i]=-1.0
print(*a)




exit()
text = input().split()
list = list(map(float,text))
for i in range(len(list)):
    if list[i]<0:
        list[i] = -1.0
print(str(enumerate(list)))

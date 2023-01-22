
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def f(k):
    p = 1
    for i in range(2, k+1):
        p *= i
    return p

n = int(input('введите натуральное число '))
list = []
list.append(1)
for i in range(1, n):
    list.append(f(i+1))
print(list)


exit() # не могу понять почему этот код выводит неправильные значения
n = int(input('введите натуральное число '))
list = []
list.append(1)
for i in range(1, n):
    list.append(list[i-1] * (i+1))
print(list)

num = int(input("Введите число : "))
a = 1
for i in range(1, num + 1):
    a *= i
    print(a, end=" ")
print()

#Вычисление факториала с помощью хвостовой рекурсии
def Factorials(n, result = 1):
    if(n<1):
        return result;
    return Factorials(n-1, n*result);

n = int(input('Введите целое число: '));

listFactorials = [];

for i in range(1, n+1):
    listFactorials.append(Factorials(i));

print(listFactorials);

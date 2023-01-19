# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n < -2:
        return fib(n+2)-fib(n+1)
    elif n == -2:
        return -1
    elif n == -1:
        return 1
    elif n == 0:
        return 0
    elif n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

a = abs(int(input('введите натуральное число ')))
list = []
for i in range(-a, a+1):
    list.append(fib(i))
print(list)


exit()
def lst_fibonacci_num():
    num = int(input('Введите любое натуральное число: '))
    fib = []
    a, b = 1, 1
    for i in range(num):
        fib.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for j in range(num + 1):
        fib.insert(0, a)
        a, b = b, a - b
    print(f'Список чисел Фибоначчи для {num}: {fib}')
lst_fibonacci_num()


def fullFibonacci(n):
    fibonacci = [0]
    if n == 0:
        return fibonacci
    elif n == 1:
        fibonacci.append(1)
    elif n > 1:
        fibonacci = fullFibonacci(n - 1)
        fibonacci.append(fullFibonacci(n - 1)[-1] + fullFibonacci(n - 2)[-1])
    fibonacci.insert(0, fibonacci[-1] * ((-1) ** (n + 1)))
    return fibonacci

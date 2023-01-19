# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('введите натуральное число '))
list = []
for i in range(2,n):
    k = False
    for j in range(2, i):
        if i % j == 0:
            k = True
            break
    if n % i == 0 and k == False:
        list.append(i)
print(list)

# от Сергея

exit()
n = int(input("Введите число N: "))
i = 2 
list = []

while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители введенного числа указаны в списке: {list}")

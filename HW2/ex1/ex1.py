

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

a = float(input('введите число '))
while a != int(a):
    a *= 10
a1 = int(a)
sum = int()
while a1 > 0:
    sum += a1 % 10
    a1 = a1 // 10
print(sum)


exit()

# От Сергей Сердюк всем 02:10 PM
n = float(input('Введите число - '))
while n % 1 > 0:
    n *= 10
summ = 0
while n > 0:
    summ += n % 10
    n //= 10
print(int(summ))


s = '0.56'
summ = 0
for i in s:
    if i.isdigit():
        summ += int(i)
print(summ)

num = str(abs(float(input("Введите число: ")))).replace(".", "")

result = 0
for i in num:
    result += int(i)

print(result)

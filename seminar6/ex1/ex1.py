# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные 
# числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде 
# последовательности оставшихся чисел в одну строчку через пробел.
# пример  - 8 11 0 -23 140 1 => 11 -23

text = list(map(int, input().split()))
lst = list(filter(lambda i: 9 < abs(i) < 100, text))
print(*lst)

exit()
print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))
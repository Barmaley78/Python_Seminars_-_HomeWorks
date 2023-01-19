# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}
import math

n = float(input('введите точность вычисления '))
a = 0
while n != int(n):
    a+=1
    n*=10
print("{:.{}f}".format(math.pi,a))

# от Сергея

exit()
a = int(input('введите нужную точность 1#= '))
pi_target = 0
for i in range(1, 1000000):
    pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
print(str(pi_target)[:a + 2])
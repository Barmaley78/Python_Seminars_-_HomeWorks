# 1 расчитать нод двух чисел (быстрый и медленный способ)

m = 45
n = 78

# быстрый способ
if m < n:
    m, n = n, m

while n!=0:
    m, n = n, m % n
print(m)

# медленный способ
exit()
while m != n:
    if m > n:
        m -= n
    else:
        n -= m
print(m)


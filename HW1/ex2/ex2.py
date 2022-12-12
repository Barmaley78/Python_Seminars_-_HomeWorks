# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) 
# для всех значений предикат.

a = [0,0,0]
for i in range(2):
    for j in range(2):
        for k in range(2):
            a[0] = i
            a[1] = j
            a[2] = k
            print(i, ' ', j, ' ', k, ' ', not(a[0] or a[1] or a[2]) == (not a[0] and not a[1] and not a[2]))

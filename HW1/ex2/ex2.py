# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) 
# для всех значений предикат.

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(i, ' ', j, ' ', k, ' ', not(i or j or k) == (not i and not j and not k))

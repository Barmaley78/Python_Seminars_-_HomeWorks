# 4)  Вводится строка. Требуется, используя введенную строку, сформировать N=10 пар кортежей в формате:
# (символ, порядковый индекс)
# Первый индекс имеет значение 0. Строка может быть короче 10 символов, а может быть и длиннее. 
# То есть, число пар может быть 10 и менее. Используя функцию zip сформируйте указанные кортежи и 
# сохраните в список с именем lst.

st = 'flivh spdijhvp sdjvp[sodjv [sodjvp[ osjdvposjhd v[poajdv[oaj sv[ojasp vjad[p ovjad'
lst = list(zip(st, range(10)))
print(lst)
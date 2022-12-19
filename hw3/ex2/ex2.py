# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [4,6,8,2,4,3,5,7]
reslist = []
if len(list) % 2 != 0:
    a = round(len(list)/2)+1
else:
    a = round(len(list)/2)
for i in range(a):
    reslist.append(list[i]*list[len(list)-1-i])
    print(i,' ',len(list)-1-i)
print(list)
print(reslist)


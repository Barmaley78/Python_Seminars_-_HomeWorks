# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
import random
random.seed()
t = int()
list = [1,2,3,4,5,6,7,8,9,0]
for i in range(len(list)):
    t = list[i]
    list.pop(i)
    list.insert(random.randint(0,9),t)
print(list)

exit()
# в питоне обмен переменных можно производить так
a,b = b,a

print(list)
shuffle(list)
print(list)

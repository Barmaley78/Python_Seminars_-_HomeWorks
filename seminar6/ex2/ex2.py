# 2. Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

a = ['a', 'b', '2', '3' ,'c']
num_list = []
char_list = []
for i in a:
    try: # обработка исключений
        int(i)
        num_list.append(i)
    except:
        char_list.append(i)
print(num_list)
print(char_list)

exit()
b= filter(str.isalpha, a)
c= filter(str.isdigit, a)

print(*b)
print(*c)

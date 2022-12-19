# 4) Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. 
# Окончанием ввода пусть служит пустая строка.

data = open('file.txt', 'w')
while True:
    str1 = input()
    data.writelines(str1)
    if str1 == '':
        break
data.close()
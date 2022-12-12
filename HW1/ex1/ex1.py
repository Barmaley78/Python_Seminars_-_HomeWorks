# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

daynumber = int(input('введите номер дня '))
daynumber = abs(daynumber) % 7
if daynumber in range(1, 5):
    print(daynumber,end=' нет')
else:
    print(daynumber,end=' да')
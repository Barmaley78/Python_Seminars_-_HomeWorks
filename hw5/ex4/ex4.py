# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def arc(sss):
    res_str = ''
    test_char = ''
    count = 1
    if sss == '': return ''
    for c in sss:
        if c != test_char:
            if test_char:
                res_str += str(count) + test_char
            count = 1
            test_char = c
        else:
            count += 1
    else:
        res_str += str(count) + test_char
    return res_str

def unarc(sss):
    res_str = ''
    count = ''
    for c in sss:
        if c.isdigit():
            count += c
        else:
            res_str += c * int(count)
            count = ''
    return res_str


d = open('hw5_data1.txt', 'r')
s = d.read()
d.close()

print('выберите операцию ')
print('1 архивировать ')
print('2 разархивировать ')
sel = input()
if sel=='1':
    res = arc(s)
elif sel=='2':
    res = unarc(s)
else:
    print('не правильно выбрана операция')

d = open('hw5_data2.txt', 'w')
d.writelines(res)
d.close()
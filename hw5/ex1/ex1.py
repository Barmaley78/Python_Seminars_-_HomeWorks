# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = 'вмы итвуеи евткети tmtfабвyhn tmtumnt wefабвwqef etnetb'
def remove_word(s):
    if 'абв' in s:
        s = ''
    return s

a = list(map(remove_word, text.split()))
s1 = ''
for i in range(len(a)):
    if a[i] != '':
        s1 = s1 + a[i] + ' '
print(s1)

exit()
1
text = 'вмы итвуеи евткети tmtfабвyhn tmtumnt wefабвwqef etnetb'
user_input = text.split()
p_text = list(filter(lambda x: not 'абв' in x, user_input))
print(p_text)

2
string = list(map(str, input("Введите строку: ").split()))
print(*[x for x in string if "абв" not in x])

3
print(*list(filter(lambda t: not t.count('абв'), input('Enter the text: ').split())))
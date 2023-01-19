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
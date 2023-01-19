# 5.Напишите программу, удаляющую из текста все слова, содержащие "абв".

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

# задача с запретом букв

s1 = ' '.join([input(), 'запретил букву'])

unique = []

for i in s1:
    if(i not in unique and i!=' '):
        unique.append(i)


for i in sorted(unique):
    print(' '.join([s1,i]))
    s1 = s1.replace(i, '').strip()

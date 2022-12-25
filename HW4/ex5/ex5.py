# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def get_element_list(st):
    st = st.replace('-','+-')
    if st[0] == '+':
        st = st.replace('+','',1)
    ls = st.split('=')
    ls = ls[0].replace(' ','')
    ls = ls.split('+')
    return ls

def get_step_number(st):
    if 'x^' in st:
        i = st.find('^')
        n = int(st[i+1:])
    elif ('x' in st) and ('^' not in st):
        n = 1
    else:
        n = 0
    return n

def get_koef(st):
    if 'x' in st:
        i = st.find('x')
        n = int(st[:i-1])
    else:
        n = int(st)
    return n

def get_koef_list(lst):
    l = []
    k = get_step_number(lst[0])
    i = 0
    j = 0
    while i <= k:
        if get_step_number(lst[j]) != k-i:
            l.append(0)
        else:
            l.append(get_koef(lst[j]))
            j += 1
        i += 1
    return l

d1 = open('data1.txt', 'r')
str1 = d1.read()
d1.close()
d2 = open('data2.txt', 'r')
str2 = d2.read()
d2.close()
dres = open('datares.txt', 'w')
lst1 = get_element_list(str1)
lst2 = get_element_list(str2)
kl1 = get_koef_list(lst1)
kl2 = get_koef_list(lst2)
while len(kl1) != len(kl2):
    if len(kl1) > len(kl2):
        kl2.insert(0,0)
    else:
        kl1.insert(0,0)
res_st = ''
for i in range(len(kl1)):
    if len(kl1)-1-i > 1:
        res_st = res_st + str(kl1[i]+kl2[i]) + 'x^' + str(len(kl1)-1-i) + '+'
    elif len(kl1)-1-i == 1:
        res_st = res_st + str(kl1[i]+kl2[i]) + 'x' + '+'
    else:
        res_st = res_st + str(kl1[i]+kl2[i])
res_st = res_st.replace('+-','-')
res_st = res_st + '=0'
dres.writelines(res_st)
dres.close()
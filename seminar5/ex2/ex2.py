# 2 Объявите анонимную (лямбда) функцию для определения вхождения в переданную ей строку фрагмента "plr". 
#  То есть, функция должна возвращать True, если такой фрагмент присутствует в строке и False - в противном 
#  случае.

s1 = 'sjdnvlsdmc;lmswc;aowjcoppnjcvzdovbcosaihcplr'
s2 = 'plr'

find_in_string = lambda s2,s1: True if s2 in s1 else False
print(find_in_string(s2, s1))

exit()
def fff(s1, s2):
    if s2 in s1:
        print('True')
    else:
        print('False')


s1 = 'sjdnvlsdmc;lmswc;aowjcoppnjcvzdovbcosaihc'
s2 = 'plr'
fff(s1, s2)
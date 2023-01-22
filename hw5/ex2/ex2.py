# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход 
# определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
random.seed()


def turn(player, c):
    tst = False
    while not tst:
        move = input(f'{player}, Ваш ход ')
        if move.isdigit():
            a = int(move)
            if a > 0 and a < 29 and a <= c:
                print(f'Вы забрали {a} конфет')
                c -= a
                print(f'осталось {c} конфет')
                tst = True
            else:
                print('Взять можно от 1 до 28 конфет, но не больше чем осталось всего')
        else:
            print('Необходимо ввести число')
    return c

def simple_bot(c):
    if c > 28:
        move = random.randint(1,28)
    else:
        move = random.randint(1,c)
    print(f'Бот забрал {move} конфет')
    c -= move
    print(f'осталось {c} конфет')
    return c

def smart_bot(c):
    move = c % 29
    if move == 0:
        if c >28:
            move = random.randint(1,28)
        else:
            move = c
    print(f'Бот забрал {move} конфет')
    c -= move
    print(f'осталось {c} конфет')
    return c

def winner(c, dm, p1, p2):
    if c == 0:
        if dm % 2== 0:
            return p1
        else:
            return p2
    else:
        return False

def p2p():
    p1 = input('введите имя 1 игрока ')
    p2 = input('введите имя 2 игрока ')
    c = 2021
    win_check = c // 28
    move_turn = random.randint(0, 1)
    fin = False
    while not fin:
        if move_turn % 2 == 0:
            c = turn(p1, c)
        else:
            c = turn(p2, c)
        if move_turn >= win_check -1:
            pw = winner(c, move_turn, p1, p2)
            if pw:
                print(f'{pw} выиграл')
                fin = True
        move_turn += 1

def p2simple():
    p = input('введите имя игрока ')
    c = 2021
    win_check = c // 28
    move_turn = random.randint(0, 1)
    fin = False
    while not fin:
        if move_turn % 2 == 0:
            c = turn(p, c)
        else:
            c = simple_bot(c)
        if move_turn >= win_check -1:
            pw = winner(c, move_turn, p, 'бот')
            if pw:
                print(f'{pw} выиграл')
                fin = True
        move_turn += 1

def p2smart():
    p = input('введите имя игрока ')
    c = 2021
    win_check = c // 28
    move_turn = random.randint(0, 1)
    fin = False
    while not fin:
        if move_turn % 2 == 0:
            c = turn(p, c)
        else:
            c = smart_bot(c)
        if move_turn >= win_check -1:
            pw = winner(c, move_turn, p, 'бот')
            if pw:
                print(f'{pw} выиграл')
                fin = True
        move_turn += 1

print('Игроки могут брать из корзины не более 28 конфет за ход. Всего в корзине 2021 конфет.')
print('Выигрывает игрок сделавший последний ход')
print()
print('Выберите режим игры')
print('1 Человек - человек')
print('2 Человек - бот')
c1 = input()
if c1 == '1' or c1 == '2':
    if c1 == '1':
        p2p()
    else:    
        print('Выберите режим сложности')
        print('1 Человек - простой бот')
        print('2 Человек - умный бот')
        c2 = input()
        if c2 == '1':
            p2simple()
        elif c2 =='2':
            p2smart()
        else:
            print('вы ввели невалидное значение. Запустите игру еще раз')
else:
    print('вы ввели невалидное значение. Запустите игру еще раз')


exit()
from random import randint

a = int(input('Введите количество конфет'))
hod = 0
wins = {0: 'Игрок', 1: 'Бот'}
while a > 0:
    if a <= 28:
        print(f'Выиграл {wins[hod]}')
        break
    if hod % 2 == 0:
        print('Ход Игрока')
        d = int(input('Введите количество конфет, которое хотите взять'))
        a -= d
        print(f'Осталось конфет: {a}')
    else:
        print('Ход Бота')
        d = a % 29 # при а = 29 d = 0 и нужно делать доп проверку 
        a -= d
        print(f'Осталось конфет: {a}')
    hod = (hod + 1) % 2
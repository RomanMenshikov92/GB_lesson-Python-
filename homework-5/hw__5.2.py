
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""



import os
os.system('cls||clear')

print('Создайте программу для игры с конфетами человек против человека..\n')

from random import randint

print('Начинаем игру\n')


def playAgainstMan():
    maxCandy = 2021
    takeLimit = 28
    count = 0
    firstPlayer = input('\nВведите имя для первого игрока:  ')
    secondPlayer = input('\nВведите имя для второго игрока:  ')

    print(f'\n{firstPlayer} и {secondPlayer}, определяем рандомно кто начнет первый')

    x = randint(1, 2)
    if x == 1:
        first = firstPlayer
        second = secondPlayer
    else:
        first = secondPlayer
        second = firstPlayer

    print(f'\n{first}, вы начинаете первый ход! Всего {maxCandy} конфет')

    while maxCandy > 0:

        if count == 0:
            while True:
                try:
                    step = int(input(f'\n Ваш ход, {first}, сколько конфет берете = '))
                    break
                except ValueError:
                    print('\n ERROR! Введено не целое число, введите заново')
                    continue
            print('\n Вы ввели корректное число, продолжаем')

        if step > maxCandy or step > takeLimit:
            while True:
                try:
                    step = int(input(f'\n Только {takeLimit} и не больше конфет можно брать {first}, попробуй еще раз:  '))
                    break
                except ValueError:
                    print('\n ERROR! Введено не целое число, введите заново')
                    continue
            print('\n Вы ввели корректное число, продолжаем')
        maxCandy -= step

        if maxCandy > 0:
            print(f'\n Еще есть конфеты: {maxCandy}')
            count = 1
        else:
            print('\n Больше нет конфет')

        if count == 1:
            while True:
                try:
                    step = int(input(f'\n Ваш ход, {second}, сколько конфет берете = '))
                    break
                except ValueError:
                    print('\n ERROR! Введено не целое число, введите заново')
                    continue
            print('\n Вы ввели корректное число, продолжаем')

        if step > maxCandy or step > takeLimit:
            while True:
                try:
                    step = int(input(f'\n Только {takeLimit} и не больше конфет можно брать {second}, попробуй еще раз: '))
                    break
                except ValueError:
                    print('\n Введено не целое число, введите заново')
                    continue
            print('\n Вы ввели корректное число, продолжаем')
        maxCandy -= step

        if maxCandy > 0:
            print(f'\n Еще есть конфеты: {maxCandy}')
            count = 0
        else:
            print('\n Больше нет конфет')

    if count == 1:
        print(f'\n {first}, вы победили')
    if count == 0:
        print(f'\n {second}, вы победили')

# playAgainstMan()


def playAgainstBot():
    maxCandy = 2021
    takeLimit = 28
    firstPlayer = input('\nВведите имя для первого игрока: ')
    secondPlayer = 'Компьютер'
    players = [firstPlayer , secondPlayer]

    print(f'\n{firstPlayer} и {secondPlayer}, определяем рандомно кто начнет первый')

    first = randint(-1, 0)

    print(f'\n{players[first + 1]}, вы начинаете первый ход!')

    while maxCandy > 0:
        first += 1

        if players[first % 2] == 'Компьютер':
            print(f'\nХодит {players[first % 2]}. \nВсего {maxCandy} конфет')

            if maxCandy < 29:
                step = maxCandy
            else:
                delete = maxCandy // 28
                step = maxCandy - ((delete * takeLimit) + 1)
                if step == -1:
                    step = takeLimit -1
                if step == 0:
                    step = takeLimit
            while step > 28 or step < 1:
                step = randint(1,28)
            print(f'\n{players[first % 2]} взял {step}.')

        else:
            while True:
                try:
                    step = int(input(f'\nВаш ход {players[first % 2]}. \nВсего {maxCandy} конфет. Ваш ход:  '))
                    break
                except ValueError:
                    print('\n ERROR! Введено не целое число, введите заново')
                    continue
            print('\n Вы ввели корректное число, продолжаем')

            while step > takeLimit or step > maxCandy:
                while True:
                    try:
                        step = int(input(f'\n Только {takeLimit} и не больше конфет можно брать, попробуй еще раз:  '))
                        break
                    except ValueError:
                        print('\n ERROR! Введено не целое число, введите заново')
                        continue
                print('\n Вы ввели корректное число, продолжаем')                       
        maxCandy -= step

    print(f'Всего {maxCandy} \nПобедил {players[first % 2]}')

# playAgainstBot()

def switch():
    sw = str(input('Для начала выберете, против кого хотите играть: (man или bot): '))
    if sw == 'man':
        print(f'\nЧеловек против человека. Начнем!\n')
        playAgainstMan()
    elif sw == 'bot':
        print(f'\nЧеловек против бота. Начнем!\n')
        playAgainstBot()
    else: 
        print(f'\nНе будем играть. Некорректный выбор!\n')
        exit()
switch()

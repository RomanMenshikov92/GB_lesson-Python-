import os
from tictactoe import Board
import emoji

os.system('cls||clear')

print('Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP\n')


def ttt(board):

    i = 0
    print('----------------------------------\n')
    print(board)
    print('\n----------------------------------')
    print(emoji.emojize(':smirk:', language='alias'))
    print(f'Ходит первый игрок (Х)\n')
    while i <= 9:
        try:
            row = int(
                input('Введите строку x (от 0 до 2): '))
            col = int(
                input('Введите столбец y (от 0 до 2): '))

            if board.is_empty((row, col)):
                board.push((row, col))
                if board.result() == 1:
                    print('----------------------------------\n')
                    print(f"\nПервый игрок выиграл (Х)")
                    print(emoji.emojize(':thumbs_up:', language='alias'))
                    print(board)
                    print('\n----------------------------------')
                    break
                elif board.result() == 2:
                    print('----------------------------------\n')
                    print(f"\nВторой игрок выиграл (O)")
                    print(emoji.emojize(':thumbs_up:', language='alias'))
                    print(board)
                    print('\n----------------------------------')
                    break
            else:
                print(emoji.emojize(':exclamation:', language='alias'))
                print("Занято")
                i -= 1
            i += 1
            if i == 9:
                print('----------------------------------\n')
                print(f"\nНикто не выиграл. Это ничья")
                print(emoji.emojize(':blush:', language='alias'))
                print(board)
                print('\n----------------------------------')
                break
            print(board)
        except:
            print(emoji.emojize(':frowning:', language='alias'))
            print("Некорректно")


desk = Board((3, 3), 3)
ttt(desk)

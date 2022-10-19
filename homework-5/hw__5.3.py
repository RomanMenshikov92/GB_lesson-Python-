# Создайте программу для игры в ""Крестики-нолики"".

import os
os.system('cls||clear')

print('Создайте программу для игры в ""Крестики-нолики""\n')

print('\nДобро пожаловать в игру: Крестики-нолики')

board = list(range(1, 10))


def renderingBoard(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|',
              board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 13)


def select(ticTacToe):
    valid = False
    while not valid:
        player = input(
            f'\nВыберите цифру. Куда вы хотите отметить символ "{ticTacToe}" --> \n')
        try:
            player = int(player)
        except:
            print('\nНекорректно, еще раз выберите цифру от 1 до 9')
            continue
        if player >= 1 and player <= 9:
            if (str(board[player - 1]) not in 'XO'):
                board[player - 1] = ticTacToe
                valid = True
            else:
                print('\nЯчейка занятная')
        else:
            print('\nНекорректно, еще раз выберите цифру от 1 до 9')


def checkVictory(board):
    victory = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
               (0, 3, 6), (1, 4, 7), (2, 5, 8),
               (0, 4, 8), (2, 4, 6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def gamePlay(board):
    counter = 0
    winning = False
    while not winning:
        renderingBoard(board)
        if counter % 2 == 0:
            select('X')
        else:
            select('0')
        counter += 1
        if counter > 4:
            winningPlayer = checkVictory(board)
            if winningPlayer:
                print(
                    f'\nПобедитель, тот кто отмечал символ "{winningPlayer}"')
                winning = True
                break
        if counter == 9:
            print('\nПобедителей нет. Это Ничья')
            break
    renderingBoard(board)


gamePlay(board)

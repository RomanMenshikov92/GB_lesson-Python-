import os
os.system('cls||clear')

# Задание из hw__3.4 form homework-3
print('1.Напишите программу, которая будет преобразовывать десятичное число в двоичное.')


def DecToDouble(decimal_number):
    binary_number = ''
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number


number = 45
print(DecToDouble(number))

# Задание из hw__2.5 form homework-2
print('\n2.Реализуйте алгоритм перемешивания списка.')


def list_mixing(n):
    new_list_mixing = [n[-i - 1] for i in range(0, len(n))]
    return new_list_mixing


list_input = ['b', 'a', 99, 9]
print(list_mixing(list_input))

# Задание из hw__1.1 form homework-1
print('\n3.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')


def numberDayWeek(x):
    if x == 1:
        str(print('Нет.Это понедельник'))
    elif x == 2:
        str(print('Нет.Это вторник'))
    elif x == 3:
        str(print('Нет.Это среда'))
    elif x == 4:
        str(print('Нет.Это четверг'))
    elif x == 5:
        str(print('Нет.Это пятница'))
    elif x == 6:
        str(print('Да.Это суббота'))
    elif x == 7:
        str(print('Да.Это воскресенье'))
    else:
        str(print('\nЭто число обозначает не день недели.\n'))
    return x


num = 5
print(numberDayWeek(num))

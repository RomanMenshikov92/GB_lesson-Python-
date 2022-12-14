# Урок 1. Знакомство с Python
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


import os
os.system('cls||clear')

print('Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.\n')
numberDayWeek = int(
    input('\nВведите число, которое обозначает день недели (от 1 до 7): '))

if numberDayWeek == 1:
    print('\nЭто понедельник. Рабочий день.\n')
elif numberDayWeek == 2:
    print('\nЭто вторник. Рабочий день.\n')
elif numberDayWeek == 3:
    print('\nЭто среда. Рабочий день.\n')
elif numberDayWeek == 4:
    print('\nЭто четверг. Рабочий день.\n')
elif numberDayWeek == 5:
    print('\nЭто пятница. Рабочий день.\n')
elif numberDayWeek == 6:
    print('\nЭто суббота. Да! Выходной день.\n')
elif numberDayWeek == 7:
    print('\nЭто воскресенье. Да! Выходной день.\n')
else:
    print('\nЭто число обозначает не день недели.\n')

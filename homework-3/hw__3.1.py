# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import os
os.system('cls||clear')

print('Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.\n')


list = [2, 3, 5, 9, 3]


def sumListOdd(list):
    sum = 0
    new_list = []
    for i in range(len(list)):
        if i % 2 != 0:
            new_list.append(list[i])
            sum += list[i]         

    print(f'Числа, стоящие на нечетных позициях в списке: {new_list}')
    print(f'\nСумма элементов списка, стоящих на нечётной позиции равна: {sum}\n')

sumListOdd(list)

# Задача: предложить улучшения кода для уже решённых задач:
#     С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# from random import randint

# print('Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.\n')

# n = int(input('Введите количество элементов n: '))
# list = []
# for i in range(n):
#     list.append(randint(0, 21))
# print(f'\nСписок рандомный: {list}\n')
# multi_list = []
# for i in range((len(list)+1)//2):
#     multi_list.append(list[i]*list[len(list)-1-i])
# print(
#     f'\nСписок рандомный, который сделал произведение пар чисел списка: {list}\n')
import os
os.system('cls||clear')

# list comprehension
print('Реализуйте алгоритм перемешивания списка c помощью - list comprehension')
list = [2, 3, 4, 2, 5]

def multi_list(list):
    return [list[i] * list[len(list)-1 -i] for i in range(len(list)//2 + len(list)%2)]

print(f'\nСписок рандомный, который сделал произведение пар чисел списка: {multi_list(list)}\n')
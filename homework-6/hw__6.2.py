# Задача: предложить улучшения кода для уже решённых задач:

#     С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# (HW_2.1)
# import os
# os.system('cls||clear')
# print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.\n')
# n = input('Введите число: ')
# sum = 0
# for a in n:
#     if a.isdigit():
#         sum += int(a)
# print(f'\nСумма его цифр равняется: {sum}\n')

import os
os.system('cls||clear')

# map
print('Реализуйте алгоритм перемешивания списка c помощью - MAP\n')

n = input('Введите число: ')
sum = sum(map(int, n.replace('.', '')))
print(f'\nСумма его цифр равняется: {sum}\n')



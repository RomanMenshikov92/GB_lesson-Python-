# 2.Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]



import os
os.system('cls||clear')

from random import randint

print('Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.\n')


n = int(input('Введите количество элементов n: '))
list = []
for i in range(n):
    list.append(randint(0, 21))

print(f'\nСписок рандомный: {list}\n')

multi_list = []
for i in range((len(list)+1)//2):
    multi_list.append(list[i]*list[len(list)-1-i])

print(
    f'\nСписок рандомный, который сделал произведение пар чисел списка: {list}\n')
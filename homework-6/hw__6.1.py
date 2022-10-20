# Задача: предложить улучшения кода для уже решённых задач:

#     С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# zip & enumerate

# (HW_2.5)
# import os
# os.system('cls||clear')
# print('Реализуйте алгоритм перемешивания списка.\n')
# import random
# listRandom = [random.randint(0,11) for i in range(random.randint(1,21))]
# print(f'Первоначальный рандомный список: {listRandom}\n')
# random.shuffle(listRandom)
# print(f'Финишный рандомный список после перемешивания: {listRandom}\n')


import os
os.system('cls||clear')

print('Реализуйте алгоритм перемешивания списка c помощью - ZIP & ENUMERATE\n')

import random

listRandom = [random.randint(0,11) for i in range(random.randint(1,21))]

print(f'Первоначальный рандомный список: {listRandom}\n')

x = list(enumerate(listRandom))

random.shuffle(listRandom)
random.shuffle(x)
indices, listRandom = zip(*x)

print(f'Финишный рандомный список после перемешивания: {listRandom}\n')

print(f'Финишный рандомный список индексов в списке после перемешивания: {indices}\n')



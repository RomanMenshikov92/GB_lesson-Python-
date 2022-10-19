# Урок 1. Знакомство с Python
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

import os
os.system('cls||clear')

print('Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).\n')
x = int(input('\nВведите значение х: '))
y = int(input('\nВведите значение y: '))
if x > 0 and y > 0:
    print(f'\nПри значениях x = {x} и y = {y} , то эта точка находится в плоскости 1\n')
elif x < 0 and y > 0:
    print(f'\nПри значениях x = {x} и y = {y} , то эта точка находится в плоскости 2\n')
elif x < 0 and y < 0:
    print(f'\nПри значениях x = {x} и y = {y} , то эта точка находится в плоскости 3\n')
elif x > 0 and y < 0:
    print(f'\nПри значениях x = {x} и y = {y} , то эта точка находится в плоскости 4\n')
elif x == 0 and y == 0:
    print(f'\nПри значениях x = {x} и y = {y} , то не соответствует к условиям (X ≠ 0 и Y ≠ 0)\n')
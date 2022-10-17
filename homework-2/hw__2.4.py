# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


import colorsys
import os
os.system('cls||clear')

print('Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.\n')

from random import Random, randint

n = int(input('Введите число n: '))
list = []
for i in range(n):
    list.append(randint(-n, n+1))
    
print(f'\nСписок рандомный: {list}\n')

multi = list[0] * list[-1]

print(f'Произведение элементов на указанных позициях в списке [0]*[-1]: {multi}\n')

str_pos = str(multi)

import os.path
directory = './homework-2/'
filename = "file.html"
file_path = os.path.join(directory, filename)
if not os.path.isdir(directory):
    os.mkdir(directory)
with open(file_path, 'w') as data:
    data.writelines(str_pos)
data.close()




# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
os.system('cls||clear')

print('Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.\n')


from random import randint

k = int(input('Введите натуральную степень k: '))

ratio = [randint(0,100) for i in range(k)]+[randint(1,100)]
tack = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(ratio) if j][::-1])

tack = tack.replace('x^1+', 'x+')
poly = tack.replace('x^0', '')
tack += ('','1')[poly[-1]=='+']
tack = (tack, tack[:-2])[tack[-2:]=='^1']
print(f'\nУравнение многочлена: {tack} при натуральной степени {k}\n')

str_pos = str(tack)

import os.path
directory = './homework-4/'
filename = "file_HW_4.4.txt"
file_path = os.path.join(directory, filename)
if not os.path.isdir(directory):
    os.mkdir(directory)
with open(file_path, 'w') as data:
    data.writelines(str_pos)
data.close()

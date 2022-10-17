# 5.Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import os
os.system('cls||clear')

print('Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.\n')

import os.path
directory = './homework-4/'
filename1 = "tack_1_HW_4.4.txt"
filename2 = "tack_2_HW_4.4.txt"
filenameSum = "sum_tack_HW_4.4.txt"
file_path1 = os.path.join(directory, filename1)
file_path2 = os.path.join(directory, filename2)
file_pathSum = os.path.join(directory, filenameSum)
if not os.path.isdir(directory):
    os.mkdir(directory)

with open(file_path1, 'w', encoding='utf-8') as data:
    data.write('2*x^2 + 4*x + 5 = 0')

with open(file_path2, 'w', encoding='utf-8') as data:
    data.write('10*x^2 = 0')

with open(file_path1,'r') as data:
    tack_1 = data.readline()
    list_tack_1 = tack_1.split()

with open(file_path2,'r') as data:
    tack_2 = data.readline()
    list_tack_2 = tack_2.split()

print(f'{list_tack_1} + {list_tack_2}')
sum_tack = list_tack_1 + list_tack_2

with open(file_pathSum, 'w', encoding='utf-8') as data:
    data.write(f'{list_tack_1} + {list_tack_2}')
data.close()


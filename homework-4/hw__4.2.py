# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
os.system('cls||clear')

print('Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.\n')


n = int(input("Введите число n: "))
i = 2
list = []

while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f'\nСписок простых множителей {list} от числа {n}\n')
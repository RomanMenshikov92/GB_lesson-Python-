# 1.Вычислить число c заданной точностью d

# *Пример:* 

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import os
os.system('cls||clear')

print('Вычислить число c заданной точностью d\n')

from math import pi

d =  int(input("\nВведите число для заданной точности числа Pi: "))

print(f'\nчисло Пи с заданной точностью {d} равно {round(pi, d)}')



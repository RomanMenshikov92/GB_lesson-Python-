# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
#     Определить корни
#     Найти интервалы, на которых функция возрастает
#     Найти интервалы, на которых функция убывает
#     Построить график
#     Вычислить вершину
#     Определить промежутки, на котором f > 0
#     Определить промежутки, на котором f < 0

from sympy import symbols, sin, cos
from scipy.optimize import fsolve
import numpy
import matplotlib.pyplot as plt

import os
os.system('cls||clear')

print('f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30\n')

# Определить корни
def f(x):
    return -12 * x ** 4 * numpy.sin(numpy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30

span = [-7, 7]
leftnum = min(span)
rightnum = max(span)

def decision():
    global leftnum, rightnum
    temp = leftnum
    rightnum = rightnum
    roots = []
    interval = []
    while temp < rightnum:
        if f(temp) >= 0 and f(temp + 1) <= 0:
            w = fsolve(f, temp)
            roots.append(*w)
        if f(temp) <= 0 and f(temp + 1) >= 0:
            w = fsolve(f, temp)
            roots.append(*w)
        if f(temp) > f(temp + 1) < f(temp + 2):
            interval.append(temp + 1)
        temp += 1
    roots = [round(i, 2) for i in roots]
    print(f'Корни уравнения: {roots}')
    return roots
decision()


# Найти интервалы, на которых функция возрастает и убывает
def IntervalOfFunctions(left, right):
    array = []
    temp = left
    while left < right:
        array.append([f(left), left])
        left += 0.1
    if array[0][0] > 0:
        print(f'f > 0 - {temp, right}')
        return max(array)
    else:
        print(f'f < 0 - {temp, right}')
        return min(array)


for i in decision():
    IntervalOfFunctions(i, i+1)


# Построить график
x = [x for x in range(-30, 30)]
y = [(-12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30) for
     x in range(-30, 30)]

plt.plot(x, y)
plt.grid()
plt.show()


# ОВычислить вершину и определить промежутки, на котором f > 0 и f < 0
def AscendingAndDescending():
    roots = decision()

    if len(roots) < 2:
        print('Нет вершин')
    else:
        top = []
        for i in range(len(roots) - 1):
            top.append(IntervalOfFunctions(roots[i], roots[i + 1]))
        for j in top:
            j = [round(i, 2) for i in j]
            print(f'Вершины(координаты): [{j[1]}, {j[0]}]')
        if len(top) < 2:
            print('Ошибка')
        else:
            for i in range(len(top) - 1):
                if top[i][0] > top[i + 1][0]:
                    print('Тут убывание функции')
                else:
                    print('Тут возрастание функции')
AscendingAndDescending()

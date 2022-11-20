# 1. Написать функцию-декоратор для кеширования значений функции
#    Написать функцию seq(n)
#    n = 0 ....N
#    (1 + n) ** n возвращает [x1, x2, x3, , , , xn]

# 1.1 (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)

import time
import datetime
import os
os.system('cls||clear')

print(
    '1. Написать функцию-декоратор для кеширования значений функции\nНаписать функцию seq(n)\nn = 0 ....N\n(1 + n) ** n возвращает [x1, x2, x3, , , , xn]\n')
print('1.1 (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)\n')


def dec(func):
    def div(*args, **kwargs):
        print(
            f"Кеширование значении функции при  n = {''.join(map(str, args))} составляет = ", end='')
        return func(*args, **kwargs)
    return div


def caching(func):
    cache = {}

    def div(*args):
        key = ''.join(map(str, args))
        if key not in cache:
            cache[key] = func(*args)
        print(cache)
        return cache[key]
    return div


def logger(func):
    def div(*args, **kwargs):
        logging = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        start = time.time_ns()
        lst = func(*args, **kwargs)
        finish = time.time_ns()
        res_time = finish - start
        logging += f'Общий результат это: {lst}, общее время это: {res_time} \n'
        with open('homework-10/hw__10.1/hw_10.1_log_file.log', 'a', encoding='utf-8') as data:
            data.write(logging)
        return lst
    return div


@logger
@caching
def seq(n):
    lst = [(1 + i) ** i for i in range(0, n + 1)]
    return lst


def main():
    seq(1)
    seq(2)
    seq(3)
    seq(4)
    seq(3)
    seq(2)
    seq(1)


main()

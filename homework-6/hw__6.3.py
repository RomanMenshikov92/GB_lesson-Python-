# Задача: предложить улучшения кода для уже решённых задач:

#     С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 2. Найти сумму чисел списка стоящих на нечетной позиции

# # def sumListOdd(list):
# #     sum = 0
# #     new_list = []
# #     for i in range(len(list)):
# #         if i % 2 != 0:
# #             new_list.append(list[i])
# #             sum += list[i]         
# #     print(f'Числа, стоящие на нечетных позициях в списке: {new_list}')
# #     print(f'\nСумма элементов списка, стоящих на нечётной позиции равна: {sum}\n')
# # sumListOdd(list)
import os
os.system('cls||clear')

# lambda, filter
print('Реализуйте алгоритм перемешивания списка c помощью - lambda & filter')
n = int(input('Введите количество n: '))
print(f'Сумма элементов списка, стоящих на нечетной позиции равна:{sum(list(filter(lambda x: x % 2, [x for x in range(1, n + 1)])))}')


# словарь (тип dict)
print('\nНайти сумму чисел списка стоящих на нечетной позиции c помощью - словаря') 
y = [2, 3, 5, 9, 3]
print(f'Сумма элементов списка, стоящих на нечётной позиции равна: {sum(y[1::2])}')

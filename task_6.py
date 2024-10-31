'''Задача 6: Случайная матрица
Напишите функцию, которая генерирует случайную матрицу размером m x n, заполненную случайными целыми числами в заданном
диапазоне.]'''
import random


def func_matrix(m, x, n):
    list_ = []
    for i in range(m):
        list_.append([])
        for j in range(x):
            ran = random.randint(1, n)
            list_[i].append(ran)
    return list_

result = func_matrix(5, 4, 99)
print(result)


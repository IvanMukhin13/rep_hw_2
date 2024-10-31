"""
Задача 7: Случайный выбор из списка с весами
Напишите функцию, которая принимает список элементов и соответствующий список весов, и возвращает случайный элемент
из первого списка на основе указанных весов.
"""
import random


list_animals = ['cat', ' dog', 'lion', 'crocodile']
list_weight = [4, 45, 200, 785]


def get_item(items, items_weights):
    return f' animal: {random.choices(items, weights=items_weights)[0]}'

res = get_item(list_animals, list_weight)
print(res)
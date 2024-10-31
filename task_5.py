'''
Напишите функцию, которая генерирует случайные имена (имя и фамилия) заданного количества. Имена и фамилии должны быть
выбраны случайным образом из заранее заданных списков.
'''


import random


names = ['Luba','Nadya', 'Zhanna','Marina', 'Sveta', 'Natasha']
second_names = ['Drozdova', 'Vorobeva', 'Sokolova', 'Volkova', 'Ivanova', 'Mask']


def func(number: int):
    list_ = []
    for i in range(number):
        list_.append(random.choice(names))
        list_[i] += ''.join(' ')
        list_[i] += ''.join(random.choice(second_names))
    return list_

result = func(5)
print(result)


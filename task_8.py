'''
Задача 8: Случайное предложение
Создайте функцию, которая генерирует случайное предложение, состоящее из случайных слов. Количество слов в предложении
должно быть от 5 до 15.
'''
import random


def func():
    string = 'qwertyuiopasdfghjklzxcvbnm'
    gen_str = []
    for i in range(random.randint(5, 15)):
        gen_str.append(random.choice(string))
        gen_str[i] = ''.join(random.choices(string, k=random.randint(3, 8)))
    return gen_str


res = func()
print(res)
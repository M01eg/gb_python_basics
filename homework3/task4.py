'''
 Урок 3
 Задание 4
Программа принимает действительное положительное
число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание
необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
'''

import math


def my_func(x, y):
    return x ** y

def my_func_harder(x, y):
    multiplier = x
    while y != -1:
        x = x * multiplier
        y += 1
    return 1 / x


def task4():
    print(my_func(2, -3))
    print(my_func_harder(2, -3))


if __name__ == "__main__":
    task4()

'''
 Урок 4
 Задание 6
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа,
   начиная с указанного,
б) бесконечный итератор, повторяющий элементы
   некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle()
модуля itertools.
'''

from random import randint
from itertools import count, cycle

def count_script():
    first_element = randint(0, 10)
    print(f"Результат генерации скрипта count, начиная с числа {first_element}:")
    for i in count(first_element):
        print(i)

def cycle_script():
    n_arr = randint(5, 10)
    random_list = [randint(-5, 5) for i in range(n_arr)]

    print(f"Сгенерирован список:\n{random_list}")

    c = cycle(random_list)
    print(f"Результат скрипта cycle:")
    for i in range(len(random_list)):
        print(next(c))


def task6():
    #count_script()
    cycle_script()


if __name__ == "__main__":
    task6()

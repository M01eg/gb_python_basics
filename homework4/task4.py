'''
 Урок 4
 Задание 4
Представлен список чисел. Определить элементы списка,
не имеющие повторений. Сформировать итоговый массив
чисел, соответствующих требованию. Элементы вывести
в порядке их следования в исходном списке. Для
выполнения задания обязательно использовать генератор.
'''

from random import randint
from collections import Counter

def task4():
    n_arr = randint(5, 10)
    random_list = [randint(-5, 5) for i in range(n_arr)]

    print(f"Сгенерирован список:\n{random_list}")

    number_encounters = Counter(random_list)
    print("Элементы списка, не имеющие повторений:")
    print([k for k, v in number_encounters.items() if v == 1])


if __name__ == "__main__":
    task4()

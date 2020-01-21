'''
 Урок 4
 Задание 2
Представлен список чисел. Необходимо вывести элементы
исходного списка, значения которых больше предыдущего
элемента.
Подсказка: элементы, удовлетворяющие условию, оформить
в виде списка. Для формирования списка использовать
генератор.
'''

from random import randint

def task2():
    n_arr = randint(5, 10)
    random_list = [randint(-5, 5) for i in range(n_arr)]

    print(f"Сгенерирован список:\n{random_list}")

    print("Значения списка, которые больше предыдущего элемента:")
    q = [random_list[i] for i in range(len(random_list)) if random_list[i] > random_list[i-1]]
    print(q)


if __name__ == "__main__":
    task2()

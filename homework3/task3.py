'''
 Урок 3
 Задание 3
Реализовать функцию my_func(), которая принимает три
позиционных аргумента, и возвращает сумму наибольших
двух аргументов.
'''

def my_func(number_a, number_b, number_c):
    min_arg = min(number_a, number_b, number_c)
    if min_arg == number_a:
        return number_b + number_c
    elif min_arg == number_b:
        return number_a + number_c
    else:
        return number_a + number_b


def task3():
    print(my_func(3, 5, 4))
    print(my_func(3, -5, 4))


if __name__ == "__main__":
    task3()

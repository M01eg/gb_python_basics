'''
 Урок 4
 Задание 5
Реализовать формирование списка, используя функцию
range() и возможности генератора. В список должны
войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения
всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce

def task5():
    generated_list = [element for element in range(100, 1001) if element % 2 == 0]

    mult_result = reduce((lambda a, b: a * b), generated_list)
    print(f"Результат умножения списка:\n{mult_result}")


if __name__ == "__main__":
    task5()

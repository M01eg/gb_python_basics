'''
 Урок 3
 Задание 1
Реализовать функцию, принимающую два числа (позиционные
аргументы) и выполняющую их деление. Числа запрашивать
у пользователя, предусмотреть обработку ситуации деления
на ноль.
'''

def divide(dividend, divisor):
    if divisor == 0:
        raise Exception
    return dividend / divisor


def task1():
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        result = divide(a, b)
        print(f"{a} / {b} = {result}")
    except:
        print("Error: divisor is equal to zero")


if __name__ == "__main__":
    task1()

'''
 Урок 4
 Задание 1
Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах *
ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
'''

import sys

def task1():
    n_hours, hourly_rate, bonus = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    print(f"Зарплата сотрудника равна: {n_hours * hourly_rate + bonus}")


if __name__ == "__main__":
    task1()
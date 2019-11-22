'''
 Урок 1
 Задание 1
Поработайте с переменными, создайте несколько, выведите
на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
'''

def task1():
    var1 = "Hello"
    var2 = "world"

    print(f"{var1}, {var2}!")

    varnum1 = float(input("Введите дробное число:\n"))
    varnum2 = int(input("Введите целое число:\n"))

    result_mult = varnum1 * varnum2
    result_mod = varnum1 % varnum2

    print(f"Результат произведения: {result_mult}\nРезультат вычисления остатка: {result_mod}")


    print("\nНажмите Enter чтобы продолжить...")
    input()


if __name__ == "__main__":
    task1()

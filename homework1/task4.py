'''
 Урок 1
 Задание 4
Пользователь вводит целое положительное число. Найдите самую большую цифру
в числе. Для решения используйте цикл while и арифметические операции.
'''

def task4():
    strnum = input("Данная программа ищет самую большую цифру в вашем числе.\nВведите целое положительное число:\n")

    highest_digit = int(strnum[0])
    for digit in strnum:
        if int(digit) > highest_digit:
            highest_digit = int(digit)

    print(f"Самая большая цифра: {highest_digit}")

    print("\nНажмите Enter чтобы продолжить...")
    input()



if __name__ == "__main__":
    task4()

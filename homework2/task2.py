'''
 Урок 2
 Задание 2
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
'''

def task2():
    superlist = []

    n = int(input("Введите количество элементов в вашем списке: "))

    for i in range(n):
        superlist.append(input(f"Введите элемент {i+1}: "))

    for i in range(0, n // 2 * 2, 2):
        superlist[i], superlist[i+1] = superlist[i+1], superlist[i]

    print("После обмена элементов мы получили следующий список:")
    print(superlist)


if __name__ == "__main__":
    task2()
